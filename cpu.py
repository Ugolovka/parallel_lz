import multiprocessing

def s(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    numbers = range(1000)
    with multiprocessing.Pool(processes=10) as pool:
        results = pool.map(s, numbers)
    print(results)


