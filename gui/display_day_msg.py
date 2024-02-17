import tkinter as tk ##tkinter is already downloaded for us in python! yay
from classes.class_day import day

DAY = day()  

def create_day_gui(root):
    """
    Prints the day on the gui
    
    """
   
    day_label = tk.Label(root, text=f"Day {DAY.day}", font=("Times New Roman", 30))
    day_label.pack(padx=20, pady=20)
    root.after(DAY.duration, day_label.destroy)
    DAY.update()
