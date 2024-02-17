import tkinter as tk ##tkinter is already downloaded for us in python! yay

from classes.class_coworkers import coworkers

coworkers = coworkers()
def display_shop(root):
     # Create a frame to hold the coffee shop name and logo
    shop_frame = tk.Frame(root)
    shop_frame.pack(pady=20)

    # Coffee shop name in brown
    shop_name_label = tk.Label(shop_frame, text="The Favorite Coffee Shop", font=("Times New Roman", 30), fg="brown")
    shop_name_label.grid(row=0, column=1, padx=(20, 40))

    # Coffee logos on the side
    coffee_logo_left = tk.Label(shop_frame, text="[logo]")
    coffee_logo_left.grid(row=0, column=0)
    coffee_logo_right = tk.Label(shop_frame, text="[logo]")
    coffee_logo_right.grid(row=0, column=2)

    # Create a frame to hold the menu
    menu_frame = tk.Frame(root, bg="lightbrown")
    menu_frame.pack(pady=20)
    

    # Define the menu items and their prices
    menu_items = ["Latte", "Cappuccino", "Espresso"]
    menu_prices = {"Latte": "$4.50", "Cappuccino": "$3.50", "Espresso": "$2.50"}

    # Display the menu items and prices in a grid
    for i, item in enumerate(menu_items):
        item_label = tk.Label(menu_frame, text=item, font=("Helvetica", 24))
        item_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

        price_label = tk.Label(menu_frame, text=menu_prices[item], font=("Helvetica", 24))
        price_label.grid(row=i, column=1, padx=10, pady=5, sticky="e")

    # Define the coworkers
    

    # Create a frame to hold the coworker buttons and dropdown menus
    buttons_frame = tk.Frame(root)
    buttons_frame.pack(pady=20)

    # Create buttons and dropdown menus for each coworker
    for i, coworker in enumerate(coworkers):
        # Create label for coworker
        coworker_label = tk.Label(buttons_frame, text=coworker + ":", font=("Helvetica", 24))
        coworker_label.grid(row=0, column=i, padx=10, pady=5, sticky="w")

        # Create dropdown menu for coworker
        default_choice = tk.StringVar()
        default_choice.set(coworker.order.drink)  
        dropdown = tk.OptionMenu(buttons_frame, default_choice, *menu_items)
        dropdown.config(font=("Helvetica", 16))
        dropdown.grid(row=1, column=i, padx=10, pady=5)