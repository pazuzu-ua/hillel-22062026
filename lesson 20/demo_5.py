import threading
import time


def download( page: int ):
    print( f"... start page {page}" )
    time.sleep(1)
    print( f"... end page {page}" )

pages = ( 1, 2, 3, 4, 5, 6, 7, 8 )

# ----- SEQ
print( "--- SEQ ---" )
start = time.perf_counter()

for page in pages:
    download( page )

print( f"Time: { time.perf_counter() - start } s" )

# THREADS
print( "--- THD ---" )
start = time.perf_counter()

threads = [ threading.Thread( target=download, args=( page, ) ) for page in pages ]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print( f"Time: { time.perf_counter() - start } s" )
