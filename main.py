from regex import P
from call_db import Database
from pandas import DataFrame as df

tshirt_cost_make = 4.75
tshirt_cost_sell = 15.0

# mayday_tshirt = [ "Mayday t-shirt", "tshirt", "white", tshirt_cost_make, tshirt_cost_sell ]
# dia_de_los_muertos = [ "Dia De Los Muertos", "tshirt", "white", tshirt_cost_make, tshirt_cost_sell ]

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
        print(db.view_db())
        
    user_input = int(input("What you wanna' do?"))
    
    if user_input == 1:
        add_new_stock_item()
    elif user_input == 2:
        view_all_stock_items()
    
    
    