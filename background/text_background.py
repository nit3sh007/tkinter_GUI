from  tkinter import *
root = Tk()
root.geometry('1200x800')
root.title("This is title")
title_label = Label(text ='''PX stands for Pixels that determines the actual pixels on the screen. DP and DIP is same which stands for Density Independent pixels which is based on the physical density of screen. S. SP stands for Scale independent pixels. (user choice)
It is same as dp unit but it is also scaled by the user's font size preference.''',bg="red",fg = "white", padx=32,pady=94,font="arial 9 bold",borderwidth=3,relief=SUNKEN)

#title_label.pack(side=LEFT,anchor ='sw',fill=Y )
''' TOP ,BOTTOM,LEFT, RIGHT
'''
title_label.pack(side=LEFT,anchor = "ne",fill=X)
root.mainloop()
