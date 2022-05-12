from sqlite3 import *

class database:
    def __init__(self):
        conn = connect("stock_tracker.db")
        cur 