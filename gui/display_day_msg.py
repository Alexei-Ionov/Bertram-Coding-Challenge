import tkinter as tk ##tkinter is already downloaded for us in python! yay
from classes.class_day import day
from gui.clear_display import clear_gui
DAY = day()  

def create_day_gui(root):
    """
    Prints the day on the gui
    
    """
    clear_gui(root)
    day_label = tk.Label(root, text=f"Day {DAY.day}", font=("Times New Roman", 30))
    day_label.pack(padx=20, pady=20)
    DAY.update()
