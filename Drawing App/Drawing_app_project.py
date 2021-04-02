import tkinter as tk
import os
from tkinter import Menu
from tkinter import ttk,colorchooser,filedialog
import PIL
from PIL import Image
import cv2


root = tk.Tk()
root.title("Drawing app")
root.geometry("600x600")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

btn_held = False
global penwidth
penwidth = 1

color_fg = "black"
#-------------------------------------------------------------------------------


def toolbox():
    pass

def pressed(event):
    global penwidth
    print("pressed")
    penwidth += 1

def release(event):
    global penwidth
    print("released")

def save_image():
    pass

def erase_all():
    my_canvas.delete("all")

def decrease_pen_size():
    pass

def color_picker():
    pass

def add_layers():
    pass

def remove_layers():
    pass

#-------------------------------------------------------------------------------

file_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=None)
file_menu.add_command(label="Save", command=save_image)
file_menu.add_command(label="Quit", command=root.quit)

edit_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Undo", command=None)
edit_menu.add_command(label="Redo", command=None)
edit_menu.add_command(label="Delete all", command=erase_all)

view_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="View", menu=view_menu)

view_menu.add_command(label="Full-Screen", command=None)
view_menu.add_command(label="Toggle Menu", command=None)

#-------------------------------------------------------------------------------

my_canvas = tk.Canvas(root,width=400,height=500,bg="white")
my_canvas.pack(pady=20)
my_canvas.old_cords = None

def draw_line(event):
    x = event.x
    y = event.y

    if my_canvas.old_cords:
        x1 = my_canvas.old_cords
        y1 = my_canvas.old_cords
        my_canvas.create_line(x,y,x1,y1,width=penwidth,fill = color_fg, capstyle =['round'] ,smooth = True)
    my_canvas.old_cords = x,y

def release_cord(event):
    my_canvas.old_cords = None

#-------------------------------------------------------------------------------
root.bind('<Button1-Motion>', draw_line)
root.bind('<ButtonRelease-1>', release_cord)
root.bind('<Key-rightbracket>' , pressed)
root.bind('<KeyRelease-rightbracket>' , release)


root.mainloop()
