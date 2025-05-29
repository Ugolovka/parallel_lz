from concurrent.futures import ThreadPoolExecutor
import time


start_time = time.time()
def calculate_square(x):
    time.sleep(1)  
    return x * x
 
numbers = range(100)
 
with ThreadPoolExecutor(max_workers=10) as pool:
    results = list(pool.map(calculate_square, numbers))
 
print(results)
end_time = time.time()

print(f"Время выполнения: {end_time} секунд")