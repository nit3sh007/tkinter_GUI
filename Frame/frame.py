from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Frame")


root.geometry("1100x1100")

f1 = Frame(root, bg="grey",borderwidth=6,relief = SUNKEN)
f1.pack(side=LEFT ,fill="y")
l =Label(f1,text = "LEFTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
l.pack(pady = 200)


f2 = Frame(root,bg = "red", borderwidth = 8 , relief = SUNKEN )
f2.pack(side= TOP,fill = "y")
l = Label(f2,text = "WELCOME TO THIS APP")
l.pack()

f3 = Frame(root, bg="grey",borderwidth=6,relief = SUNKEN)
f3.pack(side=RIGHT ,fill="y")
l =Label(f3,text = "RIGHTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
l.pack(pady = 200)

f4 = Frame(root, bg="grey",borderwidth=6,relief = SUNKEN)
f4.pack(side=BOTTOM ,fill="y")
l =Label(f4,text = "BOTTOMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
l.pack(pady = 200)
root.mainloop()
