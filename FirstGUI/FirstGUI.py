#import tkinter 
from tkinter import *


root=Tk()

# set height and width of GUI in MAXSIZE

root.maxsize(width=400,height=300)

#set height and width of GUI in MINSIZE
#root.minsize(width=800, height= 800)

#here text is usshown in GUI App

label = Label(root,text="My First GUI")
label.pack()
root.mainloop()

#root=Tk()
#set default height and width of GUI in userdefine size
#root.geometry("900 x 800")
#label = Label(root,text="My First GUI")
#label.pack()
#root.mainloop()