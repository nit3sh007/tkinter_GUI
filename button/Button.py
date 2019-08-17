from tkinter import *

root = Tk()
root.geometry("400x300")

#creating Frame
top_frame= Frame(root)
top_frame.pack()

botton_frame = Frame(root)
botton_frame.pack(side = BOTTOM)



button_1 = Button(top_frame,text="File",fg="blue",bg="red")
button_1.pack(side=LEFT)

button_2 = Button(top_frame,text="Edit",fg="red",bg="blue")
button_2.pack(side=LEFT)

button_3 = Button(top_frame,text="View",fg="pink",bg="yellow")
button_3.pack(side=LEFT)

button_4 = Button(top_frame,text="Help",fg="blue",bg="red")
button_4.pack(side=LEFT)

label_1 = Label(root,text="Welcome to GUI",bg="blue")
label_1.pack(side=LEFT,fill= Y)
label_2 = Label(root,text="Thanks",fg = "red",bg = "Yellow")
label_2.pack(side= BOTTOM,fill = X,padx = 50,pady = 50)

root.mainloop()
