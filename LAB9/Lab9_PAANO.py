#Romel Paano
#Subject & Section: CS26 A
#Date: 9/11/17

#    NOTE THis code will only run in PYTHON 3 IDLE Shell    #

from _thread import start_new_thread
from time import sleep
from random import randint

baboon_crossing = 0 #semaphore
baboon_west = 5 
baboon_east = 5

baboon_west =  int(input("Enter numbers of babbon in the west bound: "))
baboon_east =  int(input("Enter numbers of babbon in the east bound: "))


def crossing_east():
    
    return randint(1, baboon_east)

def crossing_west():
    
    return randint(1, baboon_west)

def time_crossed():
    sleep(randint(1, 5))


def EastBound():
    
    global baboon_crossing
    global baboon_east
    global baboon_west
    
    time_crossed()

    while baboon_crossing != 0:     #indicate if a baboons are crossing
        if baboon_crossing == 0:
            break

    baboon_crossing += 1

    crossed = crossing_east() #how many baboons will cross

    print(crossed, "Eastbound baboon crossing the rope...")

    time_crossed()
    
    baboon_east -= crossed  #deduct the number of baboons will crossed
    baboon_east += crossed  #add the number of baboons that have crossed
    baboon_crossing -= 1    #indicate that no one is crossing
    

def WestBound():

    global baboon_crossing
    global baboon_east
    global baboon_west
    
    time_crossed()

    while baboon_crossing != 0:     #indicate if a baboons are crossing
        if baboon_crossing == 0:
            break

    baboon_crossing += 1

    crossed = crossing_west() #how many baboons will cross

    print(crossed, "Westbound baboon crossing the rope...")

    time_crossed()
    
    baboon_west -= crossed  #deduct the number of baboons will crossed
    baboon_east += crossed  #add the number of baboons that have crossed
    baboon_crossing -= 1    #indicate that no one is crossing 

    
def west_baboons():
    
    while baboon_west > 0:  #will stop srossing if no more baboon
        WestBound()


    
def east_baboons():
    global boboon_east
    
    while baboon_east > 0: #will stop srossing if no more baboon
        EastBound()


def main():
    
    start_new_thread(west_baboons,())
    
    start_new_thread(east_baboons,())    


main()
