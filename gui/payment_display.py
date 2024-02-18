import tkinter as tk ##tkinter is already downloaded for us in python! yay
from gui.clear_display import clear_gui
# from gui.display_confetti import display_confetti
import random
unfortunate_coworker = ""

def get_least_paying_workers(list):
    min_names, min_paid = [], float('inf')
    for coworker in list:
        if coworker.paid_for < min_paid:
            min_names, min_paid = [coworker.name], coworker.paid_for
        elif coworker.paid_for == min_paid:
            min_names.append(coworker.name)
    return min_names
def on_button_click_make_decision(event, label, least_list, root, payment, list):
    if event.num == 1:  # Check if left mouse button was clicked
        index = random.randint(0, len(least_list) - 1)
        global unfortunate_coworker
        unfortunate_coworker = least_list[index]
        label.config(text=f"The coworker that must pay is ... {unfortunate_coworker}")
        # display_confetti(root)
        ##update list 
        for coworker in list:
           
            if coworker.name == unfortunate_coworker:
                coworker.paid_for += float(payment)
               
        unfortunate_coworker = ""

     
def display_payment(root,payment, list):

    clear_gui(root)
  
    title_frame = tk.Frame(root)
    title_frame.pack(pady=20)
    least_list = get_least_paying_workers(list)

    str_least_list = least_list[0]
    for index in range(1, len(least_list)):
        coworker = least_list[index]
        str_least_list += f", {coworker}"
    least_label = tk.Label(title_frame, text=f"The coworker(s) who've paid the least so far are:\n {str_least_list}", font=("Times New Roman", 30), fg="brown")
    least_label.grid(row=0, column=1, padx=(20, 40))

    decision_frame = tk.Frame(root)
    decision_frame.pack(pady=20)
    decision_label = tk.Label(decision_frame, text=f"To break the tie and decide who pays we will pick a random number from 0 - {len(least_list) - 1}\n These numbers represent each person in our list of least payers\n Let justice be served be clicking on the button below!", font=("Times New Roman", 20), fg="black")
    decision_label.grid(row=0, column=1, padx=(20, 40))

    # decision_button_frame = tk.Frame(root)
    # decision_button_frame.pack(pady=20)
    button = tk.Button(root, text="Super random number generator button", font=("Times New Roman", 20))
    button.pack()

    person_frame = tk.Frame(root)
    person_frame.pack(pady=20)
    person_label = tk.Label(person_frame, text=f"The coworker that must pay is ... {unfortunate_coworker}", font=("Times New Roman", 20), fg="black")
    person_label.grid(row=0, column=1, padx=(20, 40))

    button.bind("<Button-1>", lambda event, arg1=person_label, arg2=least_list, arg3=root,arg4=payment,arg5=list: on_button_click_make_decision(event, arg1, arg2, arg3,arg4,arg5))

    final_msg_frame = tk.Frame(root)
    final_msg_frame.pack(pady=20)
    final_msg_label = tk.Label(final_msg_frame, text="Once you've decided the unlucky coworker, please hit enter in the CLI below to go to the next day!")
    final_msg_label.grid(row=0, column=1, padx=(20, 40))


