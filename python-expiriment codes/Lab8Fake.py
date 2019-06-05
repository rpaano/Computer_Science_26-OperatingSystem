from random import randint
from time import sleep
import threading
from graphics import *

def main2():
    n = prime()
    print(n)
    sleep(n)
    

def prime():
    return randint(0, 3)

def women():
    sleep(2)
    women_circle1.move(100,0)
    
    women_circle2.move(100,0)

    women_circle3.move(100,0)

    women_circle4.move(100,0)

    women_circle5.move(100,0)

    women_circle6.move(100,0)

    women_circle7.move(100,0)

    women_circle8.move(100,0)
    
def men():
    sleep(2)
    count = 0
    while count < 4:
        print(e)
        count += 0
        
def main():

    try:
       _thread.start_new_thread( men, (  ) )
       _thread.start_new_thread( women, (  ) )
    except:
       print ("Error: unable to start thread")

    while 1:
       pass


win = GraphWin("Toilet", 1000, 400)
win.setBackground("black")
rect_men = Rectangle(Point(800,150), Point(830, 120))
rect_men.setOutline("blue")
rect_men.draw(win)
rect_women = Rectangle(Point(800,200), Point(830, 170))
rect_women.setOutline("yellow")
rect_women.draw(win)
ln = Line(Point(730,120), Point(730,210))
ln.setOutline("red")
ln.draw(win)

ctr_men = 0
ctr_women = 0
x_men = 15
x_women = 15
    
men_circle = Circle(Point(x_men,135), 10)
men_circle.setOutline("red")
men_circle.draw(win)
    
x_men += 100
ctr_men += 1
    
men_circle1 = Circle(Point(x_men,135), 10)
men_circle1.setOutline("Blue")
men_circle1.draw(win)
   
x_men += 100
ctr_men += 1

men_circle2 = Circle(Point(x_men,135), 10)
men_circle2.setOutline("brown")
men_circle2.draw(win)
   
x_men += 100
ctr_men += 1

men_circle3 = Circle(Point(x_men,135), 10)
men_circle3.setOutline("orange")
men_circle3.draw(win)
    
x_men += 100
ctr_men += 1

men_circle4 = Circle(Point(x_men,135), 10)
men_circle4.setOutline("purple")
men_circle4.draw(win)
    
x_men += 100
ctr_men += 1

men_circle5 = Circle(Point(x_men,135), 10)
men_circle5.setOutline("red")
men_circle5.draw(win)

x_men += 100
ctr_men += 1

men_circle6 = Circle(Point(x_men,135), 10)
men_circle6.setOutline("Blue")
men_circle6.draw(win)
    
x_men += 100
ctr_men += 1

men_circle7 = Circle(Point(x_men,135), 10)
men_circle7.setOutline("white")
men_circle7.draw(win)
    
x_men += 100
ctr_men += 1

women_circle1 = Circle(Point(x_women,185), 10)
women_circle1.setOutline("yellow")
women_circle1.draw(win)
    
x_women += 100
ctr_women += 1    

women_circle2 = Circle(Point(x_women,185), 10)
women_circle2.setOutline("yellow")
women_circle2.draw(win)
    
x_women += 100
ctr_women += 1

women_circle3 = Circle(Point(x_women,185), 10)
women_circle3.setOutline("yellow")
women_circle3.draw(win)
    
x_women += 100
ctr_women += 1
women_circle4 = Circle(Point(x_women,185), 10)
women_circle4.setOutline("yellow")
women_circle4.draw(win)
    
x_women += 100
ctr_women += 1

women_circle5 = Circle(Point(x_women,185), 10)
women_circle5.setOutline("yellow")
women_circle5.draw(win)
    
x_women += 100
ctr_women += 1

women_circle6 = Circle(Point(x_women,185), 10)
women_circle6.setOutline("yellow")
women_circle6.draw(win)
    
x_women += 100
ctr_women += 1

women_circle7 = Circle(Point(x_women,185), 10)
women_circle7.setOutline("yellow")
women_circle7.draw(win)

x_women += 100
ctr_women += 1

women_circle8 = Circle(Point(x_women,185), 10)
women_circle8.setOutline("yellow")
women_circle8.draw(win)
    
x_women += 100
ctr_women += 1
    
x_women += 100
ctr_women += 1


    
main()
win.getMouse()
