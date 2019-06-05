from time import sleep
import tkinter as tk
from random import randint
from _thread import start_new_thread

count = 0
root = tk.Tk()
x_men = 15
y_men = 135

x_women = 15
y_women = 185

def delete(men):
    canvas.delete(men)

def random_gen():
    return randint(1, 3)

def women_move():
    canvas.move(women1,100,0)

    canvas.move(women2,100,0)

    canvas.move(women3,100,0)

    canvas.move(women4,100,0)

    canvas.move(women5,100,0)

    canvas.move(women6,100,0)

    canvas.move(women7,100,0)

    canvas.move(women8,100,0)

def men_move():
    canvas.move(men1,100,0)

    canvas.move(men2,100,0)

    canvas.move(men3,100,0)

    canvas.move(men4,100,0)

    canvas.move(men5,100,0)

    canvas.move(men6,100,0)

    canvas.move(men7,100,0)

    canvas.move(men8,100,0)

def waiting():
    num = random_gen()
    print(num)
    sleep(num)

def men():
    waiting()
    print("men8_mov")
    canvas.move(men8,100,0)
    print("waiting")
    waiting()
    print("men_move")
    
    men_move()
    print("men7_mov")
    waiting()
    canvas.move(men7,100,0)
    print("waiting")
    waiting()
    print("men_move")
    
    men_move()
    print("men6_mov")
    waiting()
    canvas.move(men6,100,0)
    print("waiting")
    waiting()
    print("men_move")
    
    men_move()
    print("men5_mov")
    waiting()
    canvas.move(men5,100,0)
    print("waiting")
    waiting()
    print("men_move")

    men_move()
    print("men4_mov")
    waiting()
    canvas.move(men4,100,0)
    print("waiting")
    waiting()
    print("men_move")

    men_move()
    print("men3_mov")
    waiting()
    canvas.move(men3,100,0)
    print("waiting")
    waiting()
    print("men_move")

    men_move()
    print("men2_mov")
    waiting()
    canvas.move(men2,100,0)
    print("waiting")
    waiting()
    print("men_move")

    men_move()
    print("men1_mov")
    waiting()
    canvas.move(men1,100,0)
    print("waiting")
    waiting()
    print("men_move")
    
    men_move()

    

def women():
    
    waiting()
    print("men8_mov")
    canvas.move(women8,100,0)
    print("waiting")
    waiting()
    print("women_move")
    
    women_move()
    print("women7_mov")
    waiting()
    canvas.move(women7,100,0)
    print("waiting")
    waiting()
    print("women_move")
    
    women_move()
    print("women6_mov")
    waiting()
    canvas.move(women6,100,0)
    print("waiting")
    waiting()
    print("women_move")
    
    women_move()
    print("women5_mov")
    waiting()
    canvas.move(women5,100,0)
    print("waiting")
    waiting()
    print("women_move")

    women_move()
    print("women4_mov")
    waiting()
    canvas.move(women4,100,0)
    print("waiting")
    waiting()
    print("women_move")

    women_move()
    print("women3_mov")
    waiting()
    canvas.move(women3,100,0)
    print("waiting")
    waiting()
    print("women_move")

    women_move()
    print("women2_mov")
    waiting()
    canvas.move(women2,100,0)
    print("waiting")
    waiting()
    print("wowomen_move")

    women_move()
    print("women1_mov")
    waiting()
    canvas.move(women1,100,0)
    print("waiting")
    waiting()
    print("women_move")
    
    women_move()
    
def main(event):
    n = random_gen()
    waiting()
    men_move()
    women_move()
    start_new_thread(men,())
    start_new_thread(women,())

canvas = tk.Canvas(root, width=1000, height=300)
canvas.pack()

cr_men = canvas.create_rectangle(800,150,830,120)
cr_women = canvas.create_rectangle(800,200,830,170)

#Men
men1 = canvas.create_oval(x_men-10,y_men-10,x_men+10,y_men+10,fill='red')
x_men += 100

men2 = canvas.create_oval(x_men-10,y_men-10,x_men+10,y_men+10,fill='blue')
x_men += 100

men3 = canvas.create_oval(x_men-10,y_men-10,x_men+10,y_men+10,fill='brown')
x_men += 100

men4 = canvas.create_oval(x_men-10,y_men-10,x_men+10,y_men+10,fill='purple')
x_men += 100

men5 = canvas.create_oval(x_men-10,y_men-10,x_men+10,y_men+10,fill='yellow')
x_men += 100

men6 = canvas.create_oval(x_men-10,y_men-10,x_men+10,y_men+10,fill='blue')
x_men += 100

men7 = canvas.create_oval(x_men-10,y_men-10,x_men+10,y_men+10,fill='red')
x_men += 100

men8 = canvas.create_oval(x_men-10,y_men-10,x_men+10,y_men+10,fill='brown')
x_men += 100


#Women
women1 = canvas.create_oval(x_women-10,y_women-10,x_women+10,y_women+10,fill='green')
x_women += 100

women2 = canvas.create_oval(x_women-10,y_women-10,x_women+10,y_women+10,fill='yellow')
x_women += 100

women3 = canvas.create_oval(x_women-10,y_women-10,x_women+10,y_women+10,fill='violet')
x_women += 100

women4 = canvas.create_oval(x_women-10,y_women-10,x_women+10,y_women+10,fill='orange')
x_women += 100

women5 = canvas.create_oval(x_women-10,y_women-10,x_women+10,y_women+10,fill='pink')
x_women += 100

women6 = canvas.create_oval(x_women-10,y_women-10,x_women+10,y_women+10,fill='grey')
x_women += 100

women7 = canvas.create_oval(x_women-10,y_women-10,x_women+10,y_women+10,fill='red')
x_women += 100

women8 = canvas.create_oval(x_women-10,y_women-10,x_women+10,y_women+10,fill='orange')
x_women += 100

#TEXT
canvas.create_text(400,90,fill="darkblue",font="Times 20 italic bold",text="MEN'S LINE")
canvas.create_text(400,230,fill="darkblue",font="Times 20 italic bold",text="WOMEN'S LINE")
canvas.create_text(815,100,fill="darkblue",font="Times 10 italic bold",text="TOILET")
canvas.create_text(915,100,fill="darkblue",font="Times 10 italic bold",text="EXIT")

root.bind('<Return>',main)     
root.mainloop()
