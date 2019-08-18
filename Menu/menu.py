from tkinter import*
import tkinter.messagebox


def custom_quit():
    ans=tkinter.messagebox.askokcancel(title="Are you sure?",message = "Data may be lost")
    if (ans):
        quit()
    


def work():
    print('its working')
    
root = Tk()

root.geometry('400x300')

menu_1 = Menu(root)
root.config(menu=menu_1)
# creating first menu
file_menu = Menu(menu_1)
menu_1.add_cascade(label="File",menu=file_menu)

file_menu.add_cascade(label="New File")
file_menu.add_cascade(label="Open")
file_menu.add_cascade(label="Save")
file_menu.add_command(label="Exit",command=custom_quit)

edit_menu = Menu(menu_1)
menu_1.add_cascade(label="View",menu=edit_menu)

edit_menu.add_cascade(label="copy")
edit_menu.add_cascade(label="cut")
edit_menu.add_cascade(label="Paste")



Code_menu = Menu(menu_1)
menu_1.add_cascade(label="Code",menu=Code_menu)

Help_menu = Menu(menu_1)
menu_1.add_cascade(label="Help",menu=Help_menu)


#status Bar
status= Label(root,text="Run",bg="yellow",anchor="w",relief=SUNKEN,bd=1)

status.pack(side=BOTTOM,fill=X)




root.mainloop()
    