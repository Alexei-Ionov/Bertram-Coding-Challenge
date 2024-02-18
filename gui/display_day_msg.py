import tkinter as tk ##tkinter is already downloaded for us in python! yay
from classes.class_day import day
from gui.clear_display import clear_gui
 

def create_day_gui(root, day):
    """
    Prints the day on the gui
    
    """
    clear_gui(root)
    day_label = tk.Label(root, text=f"Day {day}", font=("Times New Roman", 60))
    day_label.pack(padx=20, pady=20)
    
