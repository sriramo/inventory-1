"""This module is the main module that gets launched when the user wants to run the 
inventory application

This module will have methods to display commandline options and menus
"""
import datetime

def application_version():
    return "v1.0"
    
def menu():
    pass

def main():
    print(f"Welcome to inventory {datetime.datetime.now()}")

if __name__ == "__main__":
    print("Welcome to Inventory")


