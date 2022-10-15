#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk

#Create an instance of tkinter frame
win = Tk()

#Set the geometry of tkinter frame
win.geometry("750x750")

#Create a canvas
canvas= Canvas(win, width= 600, height= 700)
canvas.pack()

#Load an image in the script
img= ImageTk.PhotoImage(Image.open("450249259deb5d3c2aea734fbaa39d6e.jpg"))

#Add image to the Canvas Items
canvas.create_image(10,10,anchor=NW,image=img)

win.mainloop()