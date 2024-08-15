# The most used procedure for spawning a thread using this module, is defining a subclass of the Thread class. Once you’ve done
# it, you should override the __init__ and run methods.

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name, sleep_time):
        threading.Thread.__init__(self)
        threading.Thread.__init__(self)
        self.sleep_time = sleep_time
        
    def run(self):
        print("{} start".format(self.name))
        time.sleep(self.sleep_time)
        print("{} end".format(self.name))
        
threads = [MyThread("Thread-{}".format(i), i) for i in range(1, 4)]
for t in threads:
    t.start()
