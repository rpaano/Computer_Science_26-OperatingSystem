import tkinter as tk

def move_a(event):
    canvas.move(b,10,0)
    #root.after(25, move_b)

    
root = tk.Tk()

# create canvas
canvas = tk.Canvas(root)
canvas.pack()

a = canvas.create_rectangle(0, 0, 100, 100, fill='red')
b = canvas.create_rectangle(0, 0, 100, 100, fill='blue')

root.bind('<Key>',move_a)

root.mainloop()
