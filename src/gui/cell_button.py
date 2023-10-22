from tkinter import IntVar, Checkbutton, PhotoImage


class Cellbutton(Checkbutton):
    def __init__(self, parent, row, column, side=None, *args, **kwargs):
        super().__init__(parent, indicatoron=False, *args, **kwargs)
        self.parent = parent
        self.row = row
        self.column = column
        self.var = IntVar(value=False)
        self.image = PhotoImage()
        self.config(variable=self.var, image=self.image)
        self.config(compound="center", selectcolor="#404040")
        if side:
            self.config(side=side)
            
    def config(self, side=None, *args, **kwargs):
        if side:
            kwargs["width"] = side
            kwargs["height"] = side
        super().config(*args, **kwargs)

    @property
    def value(self):
        return self.var.get()
