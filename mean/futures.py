from concurrent.futures import ThreadPoolExecutor, as_completed,ProcessPoolExecutor
from mean import *
workers = 5
number_of_times = 100

def main(workers,number_of_times):    
    with ThreadPoolExecutor(workers) as executor:
        for i in range(number_of_times):
            future = executor.submit(my_mean)
            try:           
                result = future.result(timeout=0.5)# get the result from the task 
                print(result)
            except TimeoutError:
                print('Waited too long for a result')


if __name__ == '__main__':
    main(workers,number_of_times)