import threading
import time

# fibonnaci function
def print_fib(number):
    def fib(n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) +fib(n - 2)
    print(f'fib({number}) is {fib(number)}')

# create, start, and join the threads
def fibs_with_threads():
    fortieth_thread = threading.Thread(target = print_fib, args = (40, ))
    forty_first_thread = threading.Thread(target = print_fib, args = (41,))

    fortieth_thread.start()
    forty_first_thread.start()

    fortieth_thread.join()
    forty_first_thread.join()

# time the execution
start_threads = time.time()
fibs_with_threads()
end_threads = time.time()

print(f"Threads took {end_threads - start_threads:.4f} seconds")

#fib(40) is 63245986
#fib(41) is 102334155
#Threads took 43.9043 seconds