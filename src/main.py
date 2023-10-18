from tkinter import Tk
from App import *


def main():
    root = Tk()
    app = App(root)
    app.pack(side="top", fill="both", expand=True)
    root.mainloop()
    

if __name__ == "__main__":
    main()
