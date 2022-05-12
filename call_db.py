from distutils.util import execute
from sqlite3 import *

class Database:
    def __init__(self):
        conn = connect("stock_tracker.db")
        cur = conn.cursor()
        cur.execute(
                    "CREATE TABLE IF NOT EXISTS stock("
                    "title VARCHAR(50) UNIQUE NOT NULL,"
                    "garment VARCHAR(50) NOT NULL,"
                    "colour VARCHAR(50) NOT NULL,"
                    "price_make FLOAT NOT NULL,"
                    "price_sell FLOAT NOT NULL,"
                    "profit FLOAT NOT NULL"
                    ")"
                    )
        conn.commit()
        conn.close()
        
        print("class called")
        
    def add_to_db(self, title, garment, colour, price_make, price_sell):
        self.profit = price_sell - price_make
        
        conn = connect("stock_tracker.db")
        cur = conn.cursor()
        cur.execute(
                    "INSERT INTO stock (title, garment, colour, price_make, price_sell, profit)"
                    "VALUES((?), (?), (?), (?), (?), (?))", 
                    (title, garment, colour, price_make, price_sell, self.profit)
                    )
        conn.commit()
        conn.close()
        
        print(f"New item: {title} added")
        
    def view_db(self):
        conn = connect("stock_tracker.db")
        cur = conn.cursor()
        cur.execute(
                    "SELECT * FROM stock"
                    )
        values = cur.fetchall()
        conn.commit()
        conn.close()
        
        for data in values:
            print(data)