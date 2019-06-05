from myro import * 
import thread 

init("COM7")

setIRPower(132)
global x, y, pos, d

pos = [0,0]
d = [1,0]
(x,y) = pos
useful = True
def max2(a):
    return sum(a) - min(a)

def blocked():
    return sum([max2(getObstacle()), max2(getObstacle()), max2(getObstacle())]) > 4000

def online():
    global x,y
    (xx,yy) = pos

    return yy == y and xx != x

def diag():
    global pos, x, y
    (xx,yy) = pos
    print pos
    print "I am here %d, %f, %f" % (yy >= y, yy, y)
    if yy == y and xx != x: print "I am on the line!"

def oturn(direction, aoeu):
    print "I am turning %d, %d" % (direction, aoeu)
    turnBy(direction*90, "deg")
    global d
    L = [ [1,0] , [0,1] , [-1,0] , [0,-1] ]
    d = L[(L.index(d)+direction)%4]
    wait(2)

def go():
    diag()
    if blocked(): return
    global pos, d
    pos = [sum(value) for value in zip(pos, d)] 
    forward(1,1)

def walk():
    go()

def hitObj () :
    flag = False
    flag2 = False
    turn = 0
    while not flag:
        while blocked():
            oturn(1, 1)
            turn += 1
            wait(.2)

        walk()
        if blocked():
            continue
        while not flag2:
            if blocked():
                break
            oturn(-1, 2)
            turn -= 1
            if blocked():
                break
            if turn == -1:
                while not blocked():
                    walk()
                    if online():
                        flag = flag2 = True
                        break
            else:
                walk()
                walk()
                walk()
    oturn(1, 3)
    

flag = True
while flag:
    if blocked():
        (x,y) = pos
        hitObj()
    go()
