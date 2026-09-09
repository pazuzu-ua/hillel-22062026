import threading
import time


N = 40_000_000


def burn( n ):
    while n > 0:
        n -= 1

# ----- SEQ
print( "--- SEQ ---" )
start = time.perf_counter()

burn(N)
burn(N)

print( f"Time: { time.perf_counter() - start } s" )



# ----- THD
print( "--- THD ---" )
start = time.perf_counter()

t1 = threading.Thread( target=burn, args=( N, ) )
t2 = threading.Thread( target=burn, args=( N, ) )

t1.start()
t2.start()

t1.join()
t2.join()

print( f"Time: { time.perf_counter() - start } s" )
