from tkinter import *

root = Tk()

v = IntVar()

Label(root, root.title("Options"), text="""Choose a preferred language:""",
justify = LEFT, padx = 20).pack()
Radiobutton(root,
            text="Python",
            padx = 20,
            variable = v,
            value = 1).pack(anchor=W)
Radiobutton(root,
            text="C++",
            padx = 20,
            variable = v,
            value=2).pack(anchor=W)
mainloop()
