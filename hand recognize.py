import tkinter as tk
import os

# Create the main window
root = tk.Tk()
root.title('Virtual Mouse')
canvas1 = tk.Canvas(root, width=1370, height=721, bg='light blue')
canvas1.pack()

# Fix: Corrected multiline string syntax and 'bg' typo
label1 = tk.Label(root, text="AI Virtual Mouse\n" "using\n" "HAND GESTURE RECOGNITION", bg="light blue")
label1.config(font=("Andalus", 24, 'bold'))
canvas1.create_window(660, 160, window=label1)

# Function to start virtual mouse
def mouse():
        import AIVirtualMouse  # Make sure AIVirtualMouse.py exists in the same folder
    except ModuleNotFoundError:
        print("Error: 'AIVirtualMouse.py' not found. Make sure the file exists in this folder.")

# Function to open the description file
def description():
    try:
        os.startfile("description.pdf")  # Make sure this file exists in the same folder
    except FileNotFoundError:
        print("Error: 'description.pdf' not found. Please check the file path.")

# Create buttons
button1 = tk.Button(root,
                    text='AI Virtual Mouse',
                    bd=7,
                    bg="steelblue",
                    fg="black",
                    command=mouse,
                    font=("Andalus", 12, 'bold'),
                    height=1,
                    justify="right",
                    padx=20,
                    pady=12,
                    relief="ridge")
canvas1.create_window(400, 340, window=button1)

button2 = tk.Button(root,
                    text='DESCRIPTION',
                    bd=7,
                    bg="steelblue",
                    fg="black",
                    command=description,
                    font=("Andalus", 12, 'bold'),
                    height=1,
                    justify="right",
                    padx=20,
                    pady=12,
                    relief="ridge")
canvas1.create_window(900, 340, window=button2)

# Run the GUI loop
root.mainloop()