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

in_women = 0
in_men = 0

def random_gen():
    return randint(1, 3)

def women_move_x():
    canvas.move(women1,10,0)

    canvas.move(women2,10,0)

    canvas.move(women3,10,0)

    canvas.move(women4,10,0)

    canvas.move(women5,10,0)

    canvas.move(women6,10,0)

    canvas.move(women7,10,0)

    canvas.move(women8,10,0)

def men_move_x():
    canvas.move(men1,10,0)

    canvas.move(men2,10,0)

    canvas.move(men3,10,0)

    canvas.move(men4,10,0)

    canvas.move(men5,10,0)

    canvas.move(men6,10,0)

    canvas.move(men7,10,0)

    canvas.move(men8,10,0)

def men_move():
    print("the")
    ctr = 0
    while ctr < 10:
        men_move_x()
        sleep(0.05)
        ctr += 1

def women_move():
    print("the1")
    ctr = 0
    while ctr < 10:
        women_move_x()
        sleep(0.05)
        ctr += 1



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
    
    waiting()
    men_move()
    women_move()
    start_new_thread(men,())
    start_new_thread(women,())

#Window
canvas = tk.Canvas(root, width=1000, height=300)
canvas.pack()

#Toilet
cr_men = canvas.create_rectangle(800,200,830,120,outline="brown",width=3)
#cr_women = canvas.create_rectangle(800,200,830,170)

#Men
men1 = canvas.create_oval(x_men-10,y_men-10,x_men+10,y_men+10,fill='red',outline="blue",width=3)
x_men += 100

men2 = canvas.create_oval(x_men-10,y_men-10,x_men+10,y_men+10,fill='blue',outline="blue",width=3)
x_men += 100

men3 = canvas.create_oval(x_men-10,y_men-10,x_men+10,y_men+10,fill='brown',outline="blue",width=3)
x_men += 100

men4 = canvas.create_oval(x_men-10,y_men-10,x_men+10,y_men+10,fill='purple',outline="blue",width=3)
x_men += 100

men5 = canvas.create_oval(x_men-10,y_men-10,x_men+10,y_men+10,fill='yellow',outline="blue",width=3)
x_men += 100

men6 = canvas.create_oval(x_men-10,y_men-10,x_men+10,y_men+10,fill='blue',outline="blue",width=3)
x_men += 100

men7 = canvas.create_oval(x_men-10,y_men-10,x_men+10,y_men+10,fill='red',outline="blue",width=3)
x_men += 100

men8 = canvas.create_oval(x_men-10,y_men-10,x_men+10,y_men+10,fill='brown',outline="blue",width=3)
x_men += 100


#Women
women1 = canvas.create_oval(x_women-10,y_women-10,x_women+10,y_women+10,fill='green',outline="yellow",width=3)
x_women += 100

women2 = canvas.create_oval(x_women-10,y_women-10,x_women+10,y_women+10,fill='yellow',outline="yellow",width=3)
x_women += 100

women3 = canvas.create_oval(x_women-10,y_women-10,x_women+10,y_women+10,fill='violet',outline="yellow",width=3)
x_women += 100

women4 = canvas.create_oval(x_women-10,y_women-10,x_women+10,y_women+10,fill='orange',outline="yellow",width=3)
x_women += 100

women5 = canvas.create_oval(x_women-10,y_women-10,x_women+10,y_women+10,fill='pink',outline="yellow",width=3)
x_women += 100

women6 = canvas.create_oval(x_women-10,y_women-10,x_women+10,y_women+10,fill='grey',outline="yellow",width=3)
x_women += 100

women7 = canvas.create_oval(x_women-10,y_women-10,x_women+10,y_women+10,fill='red',outline="yellow",width=3)
x_women += 100

women8 = canvas.create_oval(x_women-10,y_women-10,x_women+10,y_women+10,fill='orange',outline="yellow",width=3)
x_women += 100

#TEXT
canvas.create_text(400,90,fill="darkblue",font="Times 15 italic bold",text="MEN'S LINE")
canvas.create_text(400,230,fill="darkblue",font="Times 15 italic bold",text="WOMEN'S LINE")
canvas.create_text(815,100,fill="darkblue",font="Times 10 italic bold",text="TOILET")
canvas.create_text(915,100,fill="darkblue",font="Times 10 italic bold",text="EXIT")
canvas.create_text(400,50,fill="darkblue",font="Times 10 italic bold",text="PRESS ENTER TO START")

root.bind('<Return>',main)     
root.mainloop()
