"""
Welcome to my coffee ordering coding challenge. 

This is meant to be an interactive story-like program. 

This was my first time working with GUI's and I chose tkinter to do so after doing a little research


"""
import tkinter as tk ##tkinter is already downloaded for us in python! yay
from gui.display_day_msg import create_day_gui
from gui.display_shop import display_shop
from classes.class_coworkers import coworkers

#initalize as global to make it easier to use  
root = tk.Tk() 
root.geometry("500x500")
root.title("Let's Get Some Coffee!")
cw_list = coworkers().coworkers_list


def display_gui_sequence():
    """
    this is where all the looping happens for consequent days!
    
    """
    day = 1
    coworkers_list = cw_list
    while True: 
        create_day_gui(root, day)
        # display_shop(root, day, list, restart)
        root.after(3000, lambda:  display_shop(root, coworkers_list))  # Display shop GUI after 3 seconds
        input("Please press enter once you are ready for the next day!")
        day += 1
def on_button_click(event):
    if event.num == 1:  # Check if left mouse button was clicked
        display_gui_sequence()

def main(): 
    """
    first we will set up main menu
    """
    ##need to delete
    # day = 1 if day == None else day
    # coworkers_list = cw_list if coworkers_list == None else coworkers_list
   
    label = tk.Label(root, text="Main Menu", font=("Times New Roman", 50))
    label.pack(padx=20, pady=20)

    button = tk.Button(root, text="Click to Start the Story!")
    button.pack()

    # Bind the left mouse button click event to the on_button_click function
  
    button.bind("<Button-1>", lambda event: on_button_click(event))


    label = tk.Label(root, text="Please enlarge to full screen for better experience : )", font=("Times New Roman", 20))
    label.pack(padx=20, pady=20)
    
    
    root.mainloop()
    

if __name__ == "__main__":
    main()

