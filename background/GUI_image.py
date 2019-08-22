from tkinter import *
from PIL import Image, ImageTk


'''Download pillow moudle  for import jgp image
pip install pillow
or 
In kali linux  

pip install pillow
sudo apt-get install python3-pil python3-pil.imagetk

'''

root=Tk()
root.geometry('734x440')
 
image = Image.open("photo.jpg")
photo = ImageTk.PhotoImage(image)

nitesh_label= Label(image=photo)
nitesh_label.pack()
root.mainloop()