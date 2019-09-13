from tkinter import *

def getvals():
    print('DETAILS SUBMITTED')
    with open("record.txt","w") as f:
        f.write(f"{uservalue.get(),passvalue.get(),gendervalue.get(),cityvalue.get()}")

root = Tk()
root.geometry("500x600")
root.title("Dance class")
Label(root,text="Registration",font ="arial 13 bold",padx=10).grid(row=0,column=1)

#create lable
user = Label(root,text= "Username")
password = Label(root,text="Password")
gender = Label(root,text = "Gender")
city = Label(root,text= "City")

#pack lable in grid
user.grid()
password.grid()
gender.grid()
city.grid()

#pass value in string or char
uservalue = StringVar()
passvalue = StringVar()
gendervalue = StringVar()
cityvalue = StringVar()
confirmReg = IntVar()

#details entry 
userentry = Entry(root,textvariable = uservalue)
passentry = Entry(root,textvariable = passvalue)
genderentry = Entry(root,textvariable = gendervalue)
cityentry = Entry(root,textvariable=cityvalue)

#pack entry in grid
userentry.grid(row=1,column=1)
passentry.grid(row=2,column=1)
genderentry.grid(row=3,column=1)
cityentry.grid(row=4,column =1)

#create checkbuttons
confirService= Checkbutton(text= "confirm",variable=confirmReg)
confirService.grid(row=5,column=1)

#submit button
Button(text="submit",command=getvals).grid(row = 6)
root.mainloop()
