import tkinter as tk ##tkinter is already downloaded for us in python! yay
from gui.clear_display import clear_gui
from gui.payment_display import display_payment


menu_items = [
        ("Drink", "Small", "Medium", "Large"),
        ("Regular", "$4.50", "$5.50", "$6.50"),
        ("Latte", "$4.50", "$5.50", "$6.50"),
        ("Cappuccino", "$3.50", "$4.50", "$5.50"),
        ("Espresso", "$2.00", "$2.50", "$3.00"),
        ("Mocha", "$4.50", "$5.50", "$6.50"),
        ("Special Drink", "$6.00", "$6.50", "$7.50"),
        ("Regular (Black)", "$5.00", "$5.50", "$6.00"),
    ]
total_price_global = ""

def display_menu(menu_frame):
    # Create a frame to hold the menu
    # Define the menu items and their prices for small, medium, and large sizes
   
    for i in range(len(menu_items)):
        for j in range(len(menu_items[0])):
            font_size = 30 if (i == 0 and j == 0) else 20 if (i == 0 and j == 1) else 25 if  (i == 0 and j == 2) else 30 if (i == 0 and j == 3) else 16
            item_label = tk.Label(menu_frame, text=menu_items[i][j], font=("Helvetica", font_size), bg="#D2B48C")
            item_label.grid(row=i, column=j, padx=10, pady=5, sticky="w")
    # Display the menu items and prices in a grid

def display_drop_down(buttons_frame, list):
    associated_vars = []

    # Create buttons and dropdown menus for each coworker
    drink_to_index = {
        "Regular":0, 
        "Latte":1,
        "Cappuccino":2,
        "Espresso":3,
        "Mocha":4,
        "Special Drink":5,
        "Regular (Black)": 6
        }
    for col, coworker in enumerate(list):
        # Create label for coworker
        coworker_label = tk.Label(buttons_frame, text=coworker.name + ' ' +f"${coworker.paid_for}" + ":", font=("Helvetica", 24))
        coworker_label.grid(row=0, column=col, padx=10, pady=5, sticky="w")

        # Create a list to store all combinations of menu items and sizes
        all_combinations = []
        if coworker.order.drink != "None":
            i = drink_to_index[coworker.order.drink]
            for j in range(1, len(menu_items[0])):
                combination = f"{menu_items[i+1][0]} {menu_items[i+1][j]}"  # Combine item name and size
                all_combinations.append(combination)
        else:
            for i in range(1, len(menu_items)):
                for j in range(1, len(menu_items[0])):
                    combination = f"{menu_items[i][0]} {menu_items[i][j]}"  # Combine item name and size
                    all_combinations.append(combination)

        # Create dropdown menu for coworker with all combinations
        default_choice = tk.StringVar()
        default_choice.set(all_combinations[0])  # Set default choice
        associated_vars.append(default_choice)
        dropdown = tk.OptionMenu(buttons_frame, default_choice, *all_combinations)
        dropdown.config(font=("Helvetica", 16))
        dropdown.grid(row=1, column=col, padx=10, pady=5)
    return associated_vars
def calculate_total_price(associated_vars):
    price = 0.0
    for var in associated_vars:
        selected_value = var.get()
        price += float(selected_value[-4:])
    return str(price)
        
def on_button_click_price(event, label, associated_vars):
    if event.num == 1:  # Check if left mouse button was clicked
        global total_price_global
        total_price_global = calculate_total_price(associated_vars)
        label.config(text=f"The total price is... ${total_price_global}")
        
def on_button_click_payment(event, root, list, button_frame):
    if event.num == 1:  # Check if left mouse button was clicked
        global total_price_global
        if total_price_global != "": 
            clear_gui(button_frame)
            display_payment(root, total_price_global, list)
        else:
            print("Please select and calculate the costs first")
    
def display_shop(root, list):
     # Create a frame to hold the coffee shop name and logo
    clear_gui(root)
    shop_frame = tk.Frame(root)
    shop_frame.pack(pady=20)

    # Coffee shop name in brown
    shop_name_label = tk.Label(shop_frame, text="The Favorite Coffee Shop", font=("Times New Roman", 50), fg="brown")
    shop_name_label.grid(row=0, column=1, padx=(20, 40))
    
    
    # Create a frame to hold the menu
    menu_frame = tk.Frame(root, bg="#D2B48C") #light brown hex
    menu_frame.pack(pady=20)
    # Define the menu items and their prices
    display_menu(menu_frame)

    # Create a frame to hold the coworker buttons and dropdown menus
    buttons_frame = tk.Frame(root)
    buttons_frame.pack(pady=20)

    associated_vars = display_drop_down(buttons_frame, list)

    button = tk.Button(root, text="Let's calculate the total price", font=("Times New Roman", 20))
    button.pack()

    total_price_frame = tk.Frame(root)
    total_price_frame.pack(pady=20)

    total_price_label = tk.Label(total_price_frame, text=f"The total price is... ${total_price_global}", font=("Times New Roman", 20), fg="red")
    total_price_label.grid(pady=20)
    
    # Bind the left mouse button click event to the on_button_click function
    button.bind("<Button-1>", lambda event, arg1=total_price_label, arg2=associated_vars: on_button_click_price(event, arg1,arg2))
    
    payment_buttons_frame = tk.Frame(root)
    payment_buttons_frame.pack(pady=20)
    button = tk.Button(root, text="Click here to get the unfortunate coworker who has to pay : )", font=("Times New Roman", 20))
    button.pack()
  
    button.bind("<Button-1>", lambda event, arg1=root, arg2=list,arg3=buttons_frame: on_button_click_payment(event, arg1,arg2,arg3))
