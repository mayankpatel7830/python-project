import tkinter as tk
import os
root = tk.Tk()
root.title('Virtual Mouse')


canvas1 = tk.Canvas(root, width=1370, height=721,bg='light blue')
canvas1.pack()

label1 = tk.Label(root, text='AI Virtual Mouse \n using \n HAND GESTURE RECOGNITION',bg='light blue')
label1.config(font=("Andalus",24,'bold'))
canvas1.create_window(660,160, window=label1)

def mouse():
    import AIVirtualMouse


def description():
    os.startfile("description.pdf")

button1 = tk.Button(root, text='AI Virtual Mouse ',
                   bd=7,
                   bg="steelblue",
                   fg="black",
                   command=mouse,
                   font=("Andalus",12,'bold'),
                   height=1,
                   justify="right",
                   padx=20,
                   pady=12,
                   relief="ridge",
                   )
canvas1.create_window(400, 340, window=button1)

# button2 = tk.Button(root, bg='blue', font=('Arial', 11, 'bold'))
button2 = tk.Button(root, text='  DESCRIPTION  ',
                   bd=7,
                   bg="steelblue",
                   fg="black",
                   command=description,
                   font=("Andalus",12,'bold'),
                   height=1,
                   justify="right",
                   padx=20,
                   pady=12,
                   relief="ridge",
                   )
canvas1.create_window(900, 340, window=button2)

root.mainloop()