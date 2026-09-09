import multiprocessing
import os
import sys
import threading

print("Python version :", sys.version.split()[0])
print("Process ID     :", os.getpid())
print("Parent PID     :", os.getppid())
print("CPU cores      :", os.cpu_count())
print("Start method   :", multiprocessing.get_start_method())
print("Current thread :", threading.current_thread().name)
print("Threads alive  :", threading.active_count())
