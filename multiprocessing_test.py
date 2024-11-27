import multiprocessing
import random
import time
from datetime import datetime

def print_time():
    # Wait for a random number of seconds
    wait_time = random.uniform(0, 1)
    time.sleep(wait_time)

    # Print the current time
    print(f"Process ID: {multiprocessing.current_process().name} | Time: {datetime.now()}")

if __name__ == '__main__':
    # Create and start three processes
    processes = []
    for i in range(3):
        process = multiprocessing.Process(target=print_time, name=f'Process-{i+1}')
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()