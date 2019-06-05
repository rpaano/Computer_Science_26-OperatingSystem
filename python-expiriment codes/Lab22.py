from graphics import *

def we():
    sleep(2)
    women_circle.move(100,0)

def wr():
    sleep(1)
    women_circle.move(100,0)
    
def main():
    try:
       _thread.start_new_thread( we, (  ) )
       _thread.start_new_thread( wr, (  ) )
    except:
       print ("Error: unable to start thread")

    while 1:
       pass
    
    

win = GraphWin("Toilet", 1000, 400)
win.setBackground("black")
x_men = 15
x_women = 15
men_circle = Circle(Point(x_men,135), 10)
men_circle.setOutline("red")
men_circle.draw(win)

women_circle = Circle(Point(x_women,135), 10)
women_circle.setOutline("yellow")
women_circle.draw(win)


main()
