import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

root.geometry("+1400+650")

# remove window border
root.overrideredirect(True)

# keep window on top
root.attributes("-topmost", True)

# transparent background color
root.config(bg="black")

# load image
img = Image.open("maya.png")
img = img.resize((180,220))

photo = ImageTk.PhotoImage(img)

label = tk.Label(root, image=photo, bg="black", bd=0)
label.pack()

# make black transparent
root.wm_attributes("-transparentcolor", "black")

# drag variables
x = 0
y = 0

def start_move(event):
    global x, y
    x = event.x
    y = event.y

def do_move(event):
    root.geometry(f"+{event.x_root-x}+{event.y_root-y}")

def close_app(event):
    root.destroy()

# mouse controls
label.bind("<Button-1>", start_move)
label.bind("<B1-Motion>", do_move)
label.bind("<Button-3>", close_app)

root.mainloop()