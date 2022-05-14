
from sqlite3 import *
import os

class Database:
    def __init__(self):
        self.db = "stock_tracker.db"

        conn = connect(self.db)
        cur = conn.cursor()
        cur.execute(
                    "CREATE TABLE IF NOT EXISTS stock("
                    "id SERIAL,"
                    "title STRING UNIQUE NOT NULL,"
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
        self.title = title
        self.garment = garment
        self.colour = colour
        self.price_make = price_make
        self.price_sell = price_sell
        self.profit = self.price_sell - self.price_make
        
        conn = connect(self.db)
        cur = conn.cursor()
        cur.execute(
                    "INSERT INTO stock (title, garment, colour, price_make, price_sell, profit)"
                    "VALUES((?), (?), (?), (?), (?), (?))", 
                    (self.title.lower(), self.garment, self.colour, self.price_make, self.price_sell, self.profit)
                    )
        conn.commit()
        conn.close()
        
        print(f"New item: {title} added\nProfit: {self.profit}")
        
    def view_db(self):
        conn = connect(self.db)
        cur = conn.cursor()
        cur.execute(
                    "SELECT * FROM stock"
                    )
        values = cur.fetchall()
        conn.commit()
        conn.close()
        
        for data in values:
            return data
            
    def remove_from_db(self):
        def get_titles():
            conn = connect(self.db)
            cur = conn.cursor()
            cur.execute(
                        "SELECT title FROM stock"
                        )
            titles = cur.fetchall()
            conn.commit()
            conn.close()

            return titles

        print("---------------------------------")

        titles = get_titles()
        
        # prints list of products
        for title in titles:
            print(str(title[0]))

        print("---------------------------------")

        item_to_remove = input("What product would you like to remove?")
        
        conn = connect(self.db)
        cur = conn.cursor()
        # item_to_remove = str(item_to_remove)
        cur.execute(
                    "DELETE FROM stock WHERE title = (?)", (item_to_remove)
                    )
        conn.commit()
        conn.close()
        
        print(f"{item_to_remove} has been removed from stocklist")