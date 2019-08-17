from tkinter import *

root=Tk()

root.geometry("900x800")
label = Label(root,text="My First GUI")
label.pack()

label_2 = Label (root,text="color",fg="red",bg ="yellow")
label_2.pack()
root.mainloop()
