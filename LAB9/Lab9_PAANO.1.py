from _thread import start_new_thread
from time import sleep
from random import randint

baboon_crossing = 0
baboon_west = 5
baboon_east = 5

def crossing_west():
    global baboon_west
    return randint(1, baboon_west)

def crossing_east():
    global baboon_east
    return randint(1, baboon_east)

def sleeping():
    sleep(randint(2, 5))


def west_baboon_crossing():

    global baboon_west
    global baboon_east
    global baboon_crossing
    
    sleeping()

    while baboon_crossing != 0:
        if baboon_crossing == 0:
            break

    baboon_crossing += 1 
    baboon = crossing_west()
    baboon_west =- baboon

    print(baboon, "Westbound baboon crossing the rope...")
    sleeping()
    
    #baboon_east =+ baboon
    baboon_crossing -= 1 


    

def east_baboon_crossing():
    
    global baboon_west
    global baboon_east
    global baboon_crossing
    
    sleeping()

    while baboon_crossing != 0:
        if baboon_crossing == 0:
            break

    baboon_crossing += 1 
    baboon = crossing_east()
    baboon_east =- baboon

    print(baboon, "Eastbound baboon crossing the rope...")
    sleeping()
    
    #baboon_west =+ baboon
    baboon_crossing -= 1 


def west_baboons():
    global west_baboon
    ctr = 0
    
    while ctr < 5:
        west_baboon_crossing()
        ctr += 1

def east_baboons():
    global east_baboon
    ctr = 0
    
    while ctr < 5:
        east_baboon_crossing()
        ctr +=1


def main():
    
    start_new_thread(west_baboons,())
    
    start_new_thread(east_baboons,())
    
    
main()
