from tkinter import *

root = Tk()
root.title("Drawing app")
root.geometry("600x600")


my_canvas = Canvas(root,width=400,height=500,bg="white")
my_canvas.pack(pady=20)
my_canvas.old_cords = None

def draw_line(event):
    x = event.x
    y = event.y

    if my_canvas.old_cords:
        x1 = my_canvas.old_cords
        y1 = my_canvas.old_cords
        my_canvas.create_line(x,y,x1,y1)
    my_canvas.old_cords = x,y


root.bind('<Button-1>', draw_line)
root.mainloop()
