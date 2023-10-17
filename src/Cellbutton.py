from tkinter import Checkbutton, PhotoImage

class Cellbutton(Checkbutton):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, indicatoron=False, *args, **kwargs)
        self.image = PhotoImage()
        self.config(image=self.image, compound="center")
        self.config(selectcolor="#404040")
        
    def config(self, side=None, *args, **kwargs):
        if side:
            kwargs['width'] = side
            kwargs['height'] = side
        super().config(*args, **kwargs)
        return self
