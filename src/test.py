from tkinter import *

def on_checkbutton_clicked():
    checkbutton_state = checkbutton_var.get()
    if checkbutton_state == 1:
        print("Checkbutton is checked")
        # Perform your action when the Checkbutton is checked
    else:
        print("Checkbutton is unchecked")

root = Tk()
checkbutton_var = IntVar()
checkbutton = Checkbutton(root, text="Check me", variable=checkbutton_var, command=on_checkbutton_clicked)
checkbutton.pack()

root.mainloop()
