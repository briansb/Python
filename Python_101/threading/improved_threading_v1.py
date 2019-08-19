# https://www.simplifiedpython.net/python-threading-example/

# Made the thread additions easy to see and follow

# Procedure:
# 1: Import threading module
# 2: Create thread as threading.Thread(target=YourFunction, args=ArgumentsToTheFunction)
# 3: After creating the thread, we start it using the start() function
# :  Call the join() function to stop the thread after completion of the task.

import time
import threading
 
#First Method
def greet_them(people):
    for person in people:
        print("Hello Dear " + person + ". How are you?")
        time.sleep(0.5)
 
#Second Method
def assign_id(people):
    i = 1
    for person in people:
        print("Hey! {}, your id is {}.".format(person, i))
        i += 1
        time.sleep(0.5)
 

people = ['Richard', 'Dinesh', 'Elrich', 'Gilfoyle', 'Gevin']
 
t = time.time()

# instead of this...
# greet_them(people)
# assign_id(people)

# do this...
# Created the Threads
t1 = threading.Thread(target=greet_them, args=(people,))
t2 = threading.Thread(target=assign_id, args=(people,))
 
# Started the threads
t1.start()
t2.start()
 
# Joined (stopped) the threads
t1.join()
t2.join()

 
print("Woaahh!! My work is finished..")
print("I took " + str(time.time() - t))
