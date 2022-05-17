from database import Database
from pandas import *
from os import system

tshirt_cost_make = 4.75
tshirt_cost_sell = 15.0

mayday_tshirt = {
    "title" : "Mayday",
    "garment" : "tshirt",
    "colour" : "white",
    "price to make" : tshirt_cost_make,
    "price to sell" : tshirt_cost_sell
}

if __name__ == "__main__":
    db = Database()
    
    def add_new_stock_item():
        title = input("Title: ")
        garment = input("Garment: ")
        colour = input("Colour: ")
        price_to_make = float(input("Price to make: "))
        price_to_sell = float(input("Price to sell: "))
        
        db.add_to_db(title, garment, colour, price_to_make, price_to_sell)
        
    def view_all_stock_items():
        datas = db.view_db()
        
        #df = DataFrame(data)
        # df.index = data[0]
        
        # print(df)
    
    system("clear")
    user_input = int(input("What you wanna' do?\n"))

#    df = DataFrame(data = mayday_tshirt, index=RangeIndex)
#    print(df)
    
    def list_all_stock_items():
        items = db.view_db()
        
        item_dict = []
        item_dict.append(items)
        print(item_dict)
    
    def remove_stock_item():
        items = db.view_db()
        list_all_stock = DataFrame(data=items)
        
        # PRINT ALL ITEMS IN DB
        print(list_all_stock)
        
        user_input = input("Title of the item you'd like to remove: ")
        db.remove_from_db(user_input)
    

        print(db.remove_from_db())
   
    
    def menu():
        menu = True

        system("clear") 
        user_input = input("What you wanna' do?\n")

        while (menu):
            if user_input == "1":
                menu = False
                add_new_stock_item()
            elif user_input == "2":
                menu = False
                view_all_stock_items()
            elif user_input == "3":
                menu = False
                remove_stock_item()
            elif user_input == "4":
                menu = False
                print("This is option 4")
            else:
                continue
            
    menu()
