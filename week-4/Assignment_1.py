from time import sleep,time
from threading import *
import threading
import time

start = time.time() #count threading time
#print("start")

def do_job(number):
    sleep(3)
    print(f"Job {number} finished")


def main():
    thread_list =[]
    for i in range(5):
        T =threading.Thread(target = do_job, args = (i,))
        thread_list.append(T)
        thread_list[i].start()
    print(thread_list)

    for i in range(5): #cant use: for item in thread_list #"list indices must be not Thread"
        thread_list[i].join ()


main()
end = time.time()


#print("end")
print("Total Time =",end-start) #start 3.0154056549072266

