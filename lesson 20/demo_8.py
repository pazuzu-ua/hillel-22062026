import threading
import time


counter = 0
ITERATIONS = 10_000
N_THREAD = 4
lock = threading.Lock()


def increment():
    global counter
    for _ in range( ITERATIONS ):
        with lock:
            tmp = counter
            time.sleep(0)
            counter = tmp + 1


threads = [ threading.Thread( target=increment ) for _ in range(N_THREAD) ]
start = time.perf_counter()

for t in threads:
    t.start()

for t in threads:
    t.join()

print( f"Time: { time.perf_counter() - start } s" )
print( counter )
