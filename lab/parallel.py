import os
import time  
import concurrent.futures
from tqdm import tqdm

def f(x):
    time.sleep(0.001)  # to visualize the progress
    return x**2

def run(f, my_iter):
    with concurrent.futures.ThreadPoolExecutor() as executor:
    # with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(tqdm(executor.map(f, my_iter), total=len(my_iter)))
    return results

if __name__ == '__main__':
    num_cores = os.cpu_count()
    print(f'Number of CPU cores: {num_cores}')

    my_iter = range(100000)

    start_time = time.perf_counter()
    run(f, my_iter)
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    print(f'Elapsed time: {elapsed_time:.2f} seconds')