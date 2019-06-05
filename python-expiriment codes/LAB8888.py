import _thread
import time
from random import randint

# Define a function for the thread
def print_time(  ):
   delay  = randint(0,3)
   count = 0
   print(delay)
   while count < 5:
      time.sleep(delay)
      count += 1
      print (" %s" % (  time.ctime(time.time()) ))

def prime():
    me = randint(0,3)
    count = 0
    while count < 5:
        time.sleep(me)
        print(me)
        count += 1

# Create two threads as follows
try:
   _thread.start_new_thread( print_time, (  ) )
   _thread.start_new_thread( prime, (  ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass




