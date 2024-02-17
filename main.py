"""
Welcome to my coffee ordering coding challenge. 

This is meant to be an interactive story-like program. 

This was my first time working with GUI's and I chose tkinter to do so after doing a little research

I hope you enjoy the story as much as I had fun learning how to make it : )

"""
import tkinter as tk ##tkinter is already downloaded for us in python! yay
from gui.display_day_msg import create_day_gui
from gui.display_shop import display_shop
def clear_gui(root):
    """
    first clear the gui for use 
    note: seems kind of wasteful to clear it everytime but it allows for continious flow of my gui which I like. 
    """
    for widget in root.winfo_children(): 
        widget.destroy()

def display_gui_sequence(root):
    clear_gui(root)
    create_day_gui(root)
    clear_gui(root)
    display_shop(root)

def main(): 
    """
    first we will set up main menu
    """
    root = tk.Tk() 
    root.geometry("500x500")
    root.title("Let's Get Some Coffee!")
    label = tk.Label(root, text="Main Menu", font=("Times New Roman", 50))
    label.pack(padx=20, pady=20)

    button = tk.Button(root, text="Start!", font=("Times New Roman", 20))
    button.pack(padx=20, pady=20)
    display_gui_sequence(root)
    

   

    root.mainloop()
    

if __name__ == "__main__":
    main()

