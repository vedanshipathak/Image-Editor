#tkinter is a py library used to create GUI
import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image,ImageOps,ImageTk,ImageFilter
#root will the main screen 
root=tk.Tk()
#give dimensions to the screen you want
#use .geometry for that 
root.geometry("1000x600")#length and breadth of main screen
root.title("Image Editor")#give title to the project
root.config(bg="white")#give background color grey or whatever you want

#to create the side pannel we will use Frame: frame is used for child parts
left_frame=tk.Frame(root,width=200,height=600,bg="white")
#tk.Frame(root,...) root tells about parent window inside that we create a child frame
left_frame.pack(side="left",fill="y")#want on left size and take up entire space in y direction

#function of add_img
def add_image():
  global file_path #so that we can modify it throughout the program
  file_path=filedialog.askopenfilename(initialdir="D:/codefirst.io/Tkinter Image Editor/Pictures")#initialdir will determine the path that will open when you fetch the imgs
  image=Image.open(file_path)#selecting an img from file
  #before changing it and putting to canvas we first resize it
  width,height=int(image.width/2),int(image.height/2)
  image=image.resize((width,height),Image.Resampling.LANCZOS)#.Resampling.LANCZO :related to sampling resizing method 
  canvas.config(width=image.width,height=image.height)#resizing the canvas depending upon the image
  image=ImageTk.PhotoImage(image)
  
  #set it to the canvas
  canvas.image=image
  canvas.create_image(0,0,image=image,anchor="nw")#0,0 coordinates or origin of canvas nw means right in center


#add button 
image_button=tk.Button(left_frame,text="Add Image",bg="white",command=add_image)#command will call the add_img function 
image_button.pack(pady=15)#add padding in y or spaces

#create canvas where images get imported
canvas=tk.Canvas(root,width=750,height=600)
canvas.pack()
#to start drawing on the canvas


root.mainloop()#mainloop is an infinite loop that will run until you terminate it
