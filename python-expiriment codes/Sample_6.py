import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=1000, height=300)
canvas.pack()


x_men = 515
y_men = 135

x_women = 515
y_women = 185

cr_men = canvas.create_rectangle(800,200,830,120,outline="brown",width=3)

cr_men = canvas.create_oval(x_men-10,y_men-10,x_men+10,y_men+10,fill='red',outline="blue",width=3)

def main(event):
    global cr_men
    canvas.move(cr_men[0],100,0)

root.bind('<Return>',main)   
root.mainloop()
