import tkinter as tk


root = tk.Tk()

canvas = tk.Canvas(root, width=1000, height=300)
canvas.pack()

canvas.create_text(100,10,fill="darkblue",font="Times 10 italic bold",text="Click the bubbles that are multiples of two.")
window.mainloop()
