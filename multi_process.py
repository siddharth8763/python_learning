# multiprocessing module on Windows requires the 
# if __name__ == '__main__': guard to prevent the recursive 
# spawning of processes. Without this guard, 
# the script attempts to import itself multiple times, 
# leading to the RuntimeError.

from multiprocessing import Process
import os
import time
import psutil  # Import psutil for resource monitoring

def square_nums():
    for i in range(10**7):  # Perform a large number of computations
        i * i
        # time.sleep(0.1)

def monitor_resources():
    """Monitor and print resource usage of the current process."""
    process = psutil.Process(os.getpid())
    while True:
        # Get memory and CPU usage
        memory_info = process.memory_info()
        cpu_percent = process.cpu_percent(interval=1)
        print(f"Memory Usage: {memory_info.rss / (1024 * 1024):.2f} MB | CPU Usage: {cpu_percent:.2f}%")
        time.sleep(1)

if __name__ == '__main__':
    processes = []
    num_processes = os.cpu_count()

    # Start a separate process for resource monitoring
    monitor_process = Process(target=monitor_resources)
    monitor_process.start()

    # Create processes
    for i in range(num_processes):
        p = Process(target=square_nums)
        processes.append(p)

    # Start processes
    for p in processes:
        p.start()

    # Join processes
    for p in processes:
        p.join()

    # Terminate the monitor process
    monitor_process.terminate()

    print("End main")