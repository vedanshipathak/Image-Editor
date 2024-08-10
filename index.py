#tkinter is a py library used to create GUI
import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image,ImageOps,ImageTk,ImageFilter
from tkinter import ttk


#root will the main screen 
root=tk.Tk()

#give dimensions to the screen you want
#use .geometry for that 
root.geometry("1000x600")#length and breadth of main screen
root.title("Image Editor")#give title to the project
root.config(bg="white")#give background color grey or whatever you want


pen_color = "black"
pen_size = 5
file_path = ""

#to create the side pannel we will use Frame: frame is used for child parts
left_frame=tk.Frame(root,width=200,height=600,bg="white")
#tk.Frame(root,...) root tells about parent window inside that we create a child frame
left_frame.pack(side="left",fill="y")#want on left size and take up entire space in y direction


#function of add_img
def add_image():
  global file_path #so that we can modify it throughout the program
  file_path=filedialog.askopenfilename(initialdir="C:/Users/vedanshi-Personal/Desktop")#initialdir will determine the path that will open when you fetch the imgs
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

#DRAW FUNC
def draw(event):
  x1,y1=(event.x-pen_size),(event.y-pen_size)
  x2,y2=(event.x+pen_size),(event.y+pen_size)
  canvas.create_oval(x1,y1,x2,y2,fill=pen_color,outline='')

#draw on top of the image
canvas.bind("<B1-Motion>",draw)#draw is the func
#when you click and drag you call the func draw

#function for change_color
def change_color():
  global pen_color
  pen_color=colorchooser.askcolor(title="Select pen color")[1]
  



#changing color of the pen
#we create a button
color_button=tk.Button(left_frame,text="Change pen color",command=change_color,bg="white")
color_button.pack(pady=5,padx=15)

#changing the pen size:current-5 is med 
#to do this we will create another frame inside left_frame and inside that we will add 3 radio buttons for size option
pen_size_frame=tk.Frame(left_frame,bg="white")
pen_size_frame.pack(pady=5)

#change_size function 
def change_size(size):
  global pen_size
  pen_size=size


#radio button
pen_size_1=tk.Radiobutton(pen_size_frame,text="Small",value=3,command=lambda:change_size(3),bg="white")#size of pen will be 3 small
#COMMAND CALLS THE CHANGE_SIZE FUNCTION

#LAMDA - is necessary if you want to pass arguments to the function

pen_size_1.pack(side="left")

pen_size_2=tk.Radiobutton(pen_size_frame,text="Medium",value=5,command=lambda:change_size(5),bg="white")#size of pen will be 5 medium
pen_size_2.pack(side="left")

pen_size_2.select()# if we dont write this we see both med and large are selected IT WILL SPECIFY THE PARTICULAR BTN THAT IS SELECTED AS DEFAULT

pen_size_3=tk.Radiobutton(pen_size_frame,text="Large",value=7,command=lambda:change_size(7),bg="white")#size of pen will be 7 large
pen_size_3.pack(side="left")

# to clear the drawing you created
def clear_canvas():
  canvas.delete("all")#but it will also delete the image you were drawing upon 
  #so to keep the image
  canvas.create_image(0,0,image=canvas.image,anchor="nw")


#create a button
clear_button=tk.Button(left_frame,text="Clear",command=clear_canvas,bg="#FF9797")
clear_button.pack(pady=10)


#adding filters to the image 
#to do this we will use the PILLOW library 

# add a drop down menu to show all edits
filter_label=tk.Label(left_frame,text="Select Filter",bg="white")
filter_label.pack()

#create combo box that will have options
#ttk=theme tkinter
filter_combobox=ttk.Combobox(left_frame,values=["Black and White","Blur","Emboss","Sharpen","Smooth"])
filter_combobox.pack()

#function
def apply_filter(filter):
  #here we neef to reopen the image
  image=Image.open(file_path)
  width, height = int(image.width / 2),int(image.height/2)
  image = image.resize((width,height),Image.Resampling.LANCZOS)
  if filter== "Black and White":
    image=ImageOps.grayscale(image)
  elif filter =="Blur":
    image = image.filter(ImageFilter.BLUR)
  elif filter == "Sharpen":
        image = image.filter(ImageFilter.SHARPEN)
  elif filter == "Smooth":
        image = image.filter(ImageFilter.SMOOTH)
  elif filter == "Emboss":
        image = image.filter(ImageFilter.EMBOSS) 
  image = ImageTk.PhotoImage(image)
  canvas.image = image
  canvas.create_image(0, 0, image=image, anchor="nw") 


#to select a particular filter from the comboox we use
#<<ComboboxSelected>>
filter_combobox.bind("<<ComboboxSelected>>",lambda event:apply_filter(filter_combobox.get()))
#apply_filter is func
#filter_combobox.get()-will give whatever you select from the combobox

#save image function
def save_image():
   #user select a location and filename
   file_path=filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("PNG files","*.png")])
   if file_path:
      #save current canvas content as img 
      #create an image object from canvas 
      canvas.postscript(file="temp.ps",colormode='color')#saves canvas as postscript file
      #convert postscript to png
      #use PIL for this-pillow
      img=Image.open("temp.ps")
      img.save(file_path,"PNG")
      #remove the temporary postscript file
      import os
      os.remove("temp.ps")

#creating a save option button for the image
save_image_button=tk.Button(left_frame,text="Save Image",bg="white",command=save_image)
save_image_button.pack(pady=10)

root.mainloop()#mainloop is an infinite loop that will run until you terminate it
