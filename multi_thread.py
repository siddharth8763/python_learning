# Threads share the same memory space, so they are lighter weight than processes. And data sharing between threds are easier.
# This example demonstrates the use of the threading module to perform CPU-bound tasks in parallel threads.
# However, due to Python's Global Interpreter Lock (GIL), threads may not achieve true
# parallelism for CPU-bound tasks. This example is primarily for educational purposes.
# In practice, for CPU-bound tasks, the multiprocessing module is often preferred.


from threading import Thread, Lock
import os
import time
import psutil  # Import psutil for resource monitoring

# example of resource monitoring with threads

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


# threads = []
# num_threads = 10

# # Start a separate process for resource monitoring
# monitor_process = Thread(target=monitor_resources)
# monitor_process.start()

# # Create processes
# for i in range(num_threads):
#     p = Thread(target=square_nums)
#     threads.append(p)

# # Start processes
# for p in threads:
#     p.start()

# # Join processes
# for p in threads:
#     p.join()

# # Terminate the monitor process
# monitor_process.terminate()

# print("End main")



#################################################
# race condition example

# database_value = 0

# def increase():
#     global database_value
#     local_copy = database_value
#     local_copy += 1
#     time.sleep(0.1)
#     database_value = local_copy

# if __name__ == '__main__':
#     print(f"Start value: {database_value}")

#     thread1 = Thread(target=increase)
#     thread2 = Thread(target=increase)

#     thread1.start()
#     thread2.start()

#     thread1.join()
#     thread2.join()

#     print(f"End value: {database_value}")   

#     print("End main")

#################################################

# using Lock prevent race condition

# database_value = 0

# def increase(lock):
#     global database_value

#     # lock.acquire()
#     # local_copy = database_value
#     # local_copy += 1
#     # time.sleep(0.1)
#     # database_value = local_copy
#     # lock.release()

#     # with context manager
#     with lock:
#         local_copy = database_value
#         local_copy += 1
#         time.sleep(0.1)
#         database_value = local_copy

# if __name__ == '__main__':

#     lock = Lock()

#     print(f"Start value: {database_value}")

#     thread1 = Thread(target=increase, args=(lock,))
#     thread2 = Thread(target=increase, args=(lock,))

#     thread1.start()
#     thread2.start()

#     thread1.join()
#     thread2.join()

#     print(f"End value: {database_value}")   

#     print("End main")

########################################################

#queue
# These are threadsafe FIFO data structures that can be used to share data between threads.
# This example demonstrates the use of a queue to distribute work among multiple threads.
# lock is used to synchronize access to shared resources (printing to console in this case).

# from threading import Thread, Lock, current_thread
# from queue import Queue
# import time

# def worker(q,lock):
#     while True:
#         value = q.get()
#         with lock:
#             print(f"Thread {current_thread().name} processing value: {value}")
#         q.task_done()

# if __name__ == '__main__':
#     q= Queue()
#     lock = Lock()

#     num_threads = 10

#     for i in range(num_threads):
#         thread=Thread(target=worker, args=(q,lock))
#         thread.daemon=True
#         thread.start()

#     for i in range(1,21):
#         q.put(i)

#     q.join()

#     print("end main")

###################################################################
