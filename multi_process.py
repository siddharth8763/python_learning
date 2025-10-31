# multiprocessing module on Windows requires the 
# if __name__ == '__main__': guard to prevent the recursive 
# spawning of processes. Without this guard, 
# the script attempts to import itself multiple times, 
# leading to the RuntimeError.

# from multiprocessing import Process
# import os
# import time
# import psutil  # Import psutil for resource monitoring

# def square_nums():
#     for i in range(10**7):  # Perform a large number of computations
#         i * i
#         # time.sleep(0.1)

# def monitor_resources():
#     """Monitor and print resource usage of the current process."""
#     process = psutil.Process(os.getpid())
#     while True:
#         # Get memory and CPU usage
#         memory_info = process.memory_info()
#         cpu_percent = process.cpu_percent(interval=1)
#         print(f"Memory Usage: {memory_info.rss / (1024 * 1024):.2f} MB | CPU Usage: {cpu_percent:.2f}%")
#         time.sleep(1)

# if __name__ == '__main__':
#     processes = []
#     num_processes = os.cpu_count()

#     # Start a separate process for resource monitoring
#     monitor_process = Process(target=monitor_resources)
#     monitor_process.start()

#     # Create processes
#     for i in range(num_processes):
#         p = Process(target=square_nums)
#         processes.append(p)

#     # Start processes
#     for p in processes:
#         p.start()

#     # Join processes
#     for p in processes:
#         p.join()

#     # Terminate the monitor process
#     monitor_process.terminate()

#     print("End main")

############################################################

# example of sharing single value between processes.


# from multiprocessing import Process, Value, Lock
# import time    

# def add_100(number, lock):
#     for i in range(100):
#         time.sleep(0.01)
#         with lock:
#             number.value+=i
        

# if __name__ == '__main__':
#     lock=Lock()
#     shared_number=Value('i', 0)
#     print('Number at beginning is', shared_number.value)

#     p1=Process(target=add_100, args=(shared_number, lock))
#     p2=Process(target=add_100, args=(shared_number, lock))
#     p1.start()
#     p2.start()

#     print('Number at beginning is', shared_number.value)

#####################################################################

# example of sharing array between processes.

# from multiprocessing import Process, Value, Lock, Array
# import time    

# def add_100(numbers, lock):
#     for i in range(100):
#         time.sleep(0.01)

#         for i in range(len(numbers)):
#             with lock:
#                 numbers[i]+=1
        

# if __name__ == '__main__':
#     lock=Lock()
#     shared_array=Array('d', [0.0, 100.0, 200.0])
#     print('Number at beginning is', shared_array[:])

#     p1=Process(target=add_100, args=(shared_array, lock))
#     p2=Process(target=add_100, args=(shared_array, lock))
#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print('Number at end is', shared_array[:])

################################################################

#example of using Queue to share data between processes.

# from multiprocessing import Process, Value, Lock, Array, Queue
# import time    

# def square(numbers, queue):
#     for i in numbers:
#         queue.put(1-1)

# def make_negative(numbers, queue):
#     for i in numbers:
#         queue.put(-1*i)
        

# if __name__ == '__main__':
#     lock=Lock()
#     numbers = range(1,6)
#     q=Queue()

#     p1=Process(target=square, args=(numbers, q))
#     p2=Process(target=make_negative, args=(numbers, q))
#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     while not q.empty():
#         print(q.get())

######################################################

# example of using Pool to manage multiple processes.

# from multiprocessing import Pool

# def Cube(n):
#     return n*n*n

# if __name__ == '__main__':
#     numbers = range(10)
#     pool = Pool()

#     result = pool.map(Cube, numbers)
#     pool.close()
#     pool.join()

#     print(result)

####################################

