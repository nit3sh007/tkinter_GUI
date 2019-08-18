#import tkinter 
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msg
import tkinter.scrolledtext as tkst

root = Tk(className="Notepad")
#dimension of Notepad
textPad =tkst.ScrolledText(root,width=600,height=600)

#give open_command which is use to select a file
def open_command():
        file = filedialog.askopenfile(parent=root,mode='rb',title="Select a File")
        if file!=None:
                contents = file.read()
                textPad.insert('1.0',contents)
                file.close()
#for saving file
def save_command():
        file=filedialog.asksaveasfile(mode='w')
        if file!=None:
                data=textPad.get('1.0',END+"-1c")
                file.write(data)
#for exit
def exit_command():
        if msg.askokcancel("Quit","Do you really want to quit?"):
                root.destroy()
#for about
def about_command():
         label = msg.showinfo('About','This Simple Text Editor which is writtten in Python by Nitesh')

#creating menu in notepad

menu_1 = Menu(root)
root.config(menu=menu_1)


# First menu 
file_menu = Menu(menu_1)
menu_1.add_cascade(label="File",menu=file_menu)

file_menu.add_cascade(label="New File")
file_menu.add_command(label="Open",command=open_command)
file_menu.add_command(label="Save",command=save_command)
file_menu.add_command(label="Exit",command=exit_command)

#Second Menu

edit_menu = Menu(menu_1)
menu_1.add_cascade(label="View",menu=edit_menu)

edit_menu.add_cascade(label="copy")
edit_menu.add_cascade(label="cut")
edit_menu.add_cascade(label="Paste")

# Third menu

Help_menu = Menu(menu_1)
menu_1.add_cascade(label="Help",menu=Help_menu)

view_menu = Menu(menu_1)
menu_1.add_command(label='About',command=about_command)

textPad.pack()
root.mainloop()    
