import threading
import time


def worker( number ):
    time.sleep(0.1)     # simulate work
    print(f"Thread {number} is done.")

thread = []

for i in range(15):
    t = threading.Thread( target=worker, args=( i, ) )
    thread.append( t )
    t.start()

for t in thread:
    t.join()
