import datetime
import sqlite3
from sqlite3 import Error
from dataclasses import dataclass
from sqlite3.dbapi2 import Cursor


@dataclass
class Sales:
    """
    This class represents sales
    """
    id: int
    product_id: int
    quantity: int
    #price: float
    created_date: str

    def __str__(self) -> str:
        return f"{self.id},{self.product_id},{self.quantity},{self.created_date}"
    
    def header() -> str:
        return "id, product_id, quantity, created_date"

    @staticmethod
    def create_salesdata_from_userinput():
        """
        This method will creates salesdata from the user input
        Returns:
          Sales
        """
        id = int(input('Enter Id: '))
        #name = input('Enter Product Name: ')
        product_id = int(input('Enter product Id: '))
        quantity = int(input('Enter quanity: '))
        date_time1=str(get_datetime())
        return Sales(id=id,product_id=product_id,quantity=quantity,created_date=date_time1)

    @staticmethod
    def get_all_sales():
        select_query = "SELECT * from sales"
        sales = list()
        with create_connection(database_file()) as connection:
            cursor = connection.cursor()
            for row in cursor.execute(select_query):
                sale = Sales(row[0],row[1], row[2], row[3])
                sales.append(sale)
        return sales
    
    """@staticmethod
    def get_all_sales_id1():
        select_query = "SELECT * from products"
        products_id = list()
        with create_connection(database_file()) as connection:
            cursor = connection.cursor()
            for row in cursor.execute(select_query):
                product =row[0]                      #
                products_id.append(product)
        #products_id_set=set(products_id)
        return products_id"""

    def sell_reduction(pquantity,quantity,id):
        """
        this method will reduce the quantity of item sold in inventory
        """
        update_statement=f'UPDATE products SET quantity={pquantity-quantity} where id={id}'
        with create_connection(database_file()) as connection:
            cursor=connection.cursor()
            cursor.execute(update_statement)
            connection.commit()
    
    def save(self):
        """
        This statement will insert the product into the database
        Raises:
                sqlite3.IntegrityError as entered product id already exists
        """
        try :
            insert_statement = f"INSERT into sales (id, product_id, quantity, created_date)  VALUES({self.id}, {self.product_id}, {self.quantity}, '{self.created_date}')"
            #Sales.quantity.sell_reduction(quantity=self.quantity)
            with create_connection(database_file()) as connection:
                cursor = connection.cursor()
                cursor.execute(insert_statement)
                connection.commit()
        except Error as e:
            print(e)
            #print(f"Input Unique Id For Product Other Than In Given Id List  {Sales.get_all_sales_id1()}") #My code
    
    
    def get_product_quantity(id): #self id need to provide
        select_query = f"SELECT quantity from products where id={id} "
        products_quantity = list()
        with create_connection(database_file()) as connection:
            cursor = connection.cursor()
            for row in cursor.execute(select_query):
                obj=row[0]
                print(obj)
                return obj
                #product =row[0]                      #
                #products_id.append(product)
        #products_id_set=set(products_id)
        #return products_id

    



def get_datetime():
    now=datetime.datetime.now()
    return now.strftime('%d/%m/%Y %H:%M:%S')

def database_file():
        """
        This function will return the database file location
        """
        return 'data/inventory.db'

def create_connection(db_file) -> sqlite3.Connection:
        """
        This method connects to the database and returns the connection
        """
        connection = None
        try:
            connection = sqlite3.connect(db_file)
            #print(sqlite3.version)
        except Error as e:
            print(e)
        return connection


def create_table(connection: sqlite3.Connection, create_table_sql: str):
        """
        This method will execute the sql for creating tables
        """
        try:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
        except Error as e:
            print(e)
        
    

@dataclass
class Product:
    """
    This class represents the product
    """
    id: int
    name: str
    price: float
    quantity: int

    def __str__(self) -> str:
        return f"{self.id},{self.name},{self.price},{self.quantity}"
    
    def header() -> str:
        return "id, name, price, quantity"
    
    


    @staticmethod
    def create_product_from_userinput():
        """
        This method will create product from the user input
        Returns:
          Product
        """
        id = int(input('Enter Id: '))
        name = input('Enter Product Name: ')
        price = float(input('Enter product price: '))
        quantity = int(input('Enter quanity: '))
        return Product(id=id, name=name,price=price,quantity=quantity)


    
    def update(self):
        """
        this method will impliment update data to database 
        """
        update_statement=f" update products set name={self.name}, price={self.price}, quantity={self.quantity}  "
        with create_connection(database_file()) as connection:
            cursor=connection.cursor()
            cursor.execute(update_statement)
            connection.commit()

    @staticmethod
    def get_all_products():
        select_query = "SELECT * from products"
        products = list()
        with create_connection(database_file()) as connection:
            cursor = connection.cursor()
            for row in cursor.execute(select_query):
                product = Product(row[0],row[1], row[2], row[3])
                products.append(product)
        return products
    
    @staticmethod
    def get_all_products_id():
        select_query = "SELECT * from products"
        products_id = list()
        with create_connection(database_file()) as connection:
            cursor = connection.cursor()
            for row in cursor.execute(select_query):
                product =row[0]                      #
                products_id.append(product)
        #products_id_set=set(products_id)
        return products_id
