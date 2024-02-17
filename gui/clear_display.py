def clear_gui(root):
    """
    first clear the gui for use 
    note: seems kind of wasteful to clear it everytime but it allows for continious flow of my gui which I like. 
    """
    for widget in root.winfo_children(): 
        widget.destroy()