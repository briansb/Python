import random
import time
# import the thread class from the thread module
from threading import Thread

class MyThread(Thread):
    # sub-class the thread class and override __init__ method
    #   to accept a 'name' argument
    def __init__(self, name):
        # Initialize the thread
        Thread.__init__(self)
        self.name = name
    
    def run(self):
        # override run method to have random sleep time
        amount = random.randint(3, 6)
        # this simulates the thread doing work
        time.sleep(amount)
        print(f"{self.name} is running")
        
def create_threads():
    # start 5 threads
    for i in range(5):
        name = "Thread #%s" % (i+1)
        my_thread = MyThread(name)
        # to start a thread must call start method
        #   then automatically calls run method...see above for override
        print(f"Started {name}")
        my_thread.start()
        # kills the thread
        # my_thread.join()
        
if __name__ == "__main__":
    create_threads()
    
