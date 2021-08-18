from models import Sales
import sqlite3
from sqlite3.dbapi2 import Error
import sales1

def initialize():
    #sql_products_create_table = """
    #CREATE TABLE IF NOT EXISTS products (
    #    id integer PRIMARY KEY,
     #   name text NOT NULL,
     #   price real NOT NULL,
    #    quantity int 
    #)
    #"""
    sql_sales_create_table = """
    CREATE TABLE IF NOT EXISTS sales (
        id integer PRIMARY KEY,
        product_id integer,
        quantity integer,
        created_date text NOT NULL,
        FOREIGN KEY (product_id) REFERENCES products(id)
        
    )
    """
    connection = sales1.create_connection(sales1.database_file())
    if connection is not None:
        #models.create_table(connection, sql_products_create_table)
       sales1.create_table(connection, sql_sales_create_table)

    connection.close()

def insert_salesdata(sales,ids):
    """
    this method insert the salesdata into to table
    """
    print("Enter product information")
    sales = sales1.Sales.create_salesdata_from_userinput()
    sales.save()
    """if sales.id in ids:
        print(f"Change the id as existing a product with same id {sales.id}.")
    else:
        sales.save()"""

def display_details(sales):
    """
    this ethod prints headers or column or attributes and values 
    """
    print(sales1.Sales.header())
    for sale in sales:
        print(str(sale))

if __name__ == '__main__':
    initialize()
    sales = sales1.Sales.get_all_sales()
    ids=[salerow.id for salerow in sales]
    while True:
        try:
            menu_choice=int(input("Enter 1 for sales insert \n2 for display sales " ))
            if menu_choice==1:
                sale = sales1.Sales.create_salesdata_from_userinput()
                #if sale.id in ids:
                    #print(f"Change the id as existing a product with same id {sale.id}.")
                    #continue
                sale.save()
                squantity=sale.quantity
                id1=sale.id
                print(sales1.Sales.get_product_quantity(id=id1))
                sales1.Sales.sell_reduction(pquantity=sales1.Sales.get_product_quantity(id=id1),quantity=squantity,id=id1)

                #sales1.Sales.sell_reduction
            elif menu_choice==2:
                display_details(sales)
            
        except Error as e:
            print(e)
        choice = input('Enter n to stop and y to continue')
        if choice == 'n':
            break