"""
Welcome to my coffee ordering coding challenge. 

This is meant to be an interactive story-like program. 

This was my first time working with GUI's and I chose tkinter to do so after doing a little research


"""
import tkinter as tk ##tkinter is already downloaded for us in python! yay
from gui.display_day_msg import create_day_gui
from gui.display_shop import display_shop

#initalize as global to make it easier to use  
root = tk.Tk() 
root.geometry("500x500")
root.title("Let's Get Some Coffee!")
def display_gui_sequence():
  
    create_day_gui(root)
    root.after(2000, lambda:  display_shop(root))  # Display shop GUI after 2 seconds
    
def on_button_click(event):
    if event.num == 1:  # Check if left mouse button was clicked
        display_gui_sequence()

def main(): 
    """
    first we will set up main menu
    """
    label = tk.Label(root, text="Main Menu", font=("Times New Roman", 50))
    label.pack(padx=20, pady=20)

    button = tk.Button(root, text="Click to Start the Story!")
    button.pack()

    # Bind the left mouse button click event to the on_button_click function
    button.bind("<Button-1>", on_button_click)


    label = tk.Label(root, text="Please enlarge to full screen for better experience : )", font=("Times New Roman", 20))
    label.pack(padx=20, pady=20)
    
    
    root.mainloop()
    

if __name__ == "__main__":
    main()

