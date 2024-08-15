import _thread as thread
import time

executed_count = 0

# Define a function for the thread
def print_time(thread_name, delay):
    global executed_count
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (thread_name, time.ctime(time.time())))
    executed_count += 1
    
    
# Create two threads
try:
    threads = [thread.start_new_thread(print_time, ("Thread-1", 2,)), thread.start_new_thread(print_time, ("Thread-2", 4,))]
except:
    print("Error: unable to start thread")
while executed_count < 2:
    pass