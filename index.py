#tkinter is a py library used to create GUI
import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image,ImageOps,ImageTk,ImageFilter
#root will the main screen 
root=tk.Tk()
#give dimensions to the screen you want
#use .geometry for that 
root.geometry("1000x700")#length and breadth of main screen
root.title("Image Editor")#give title to the project
root.config(bg="grey")#give background color grey or whatever you want

#to create the side pannel we will use Frame: frame is used for child parts
left_frame=tk.Frame(root,width=300,height=600,bg="black")
#tk.Frame(root,...) root tells about parent window inside that we create a child frame
left_frame.pack(side="left",fill="y")
root.mainloop()#mainloop is an infinite loop that will run until you terminate it