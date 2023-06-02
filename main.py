import time
import math


def calcPi():
    pi = sum(math.pow(-1, i) / (2 * i + 1) for i in range(100000000))
    pi *= 4
    return pi


start = time.time()
pi = calcPi()
end = time.time()
print(pi)
print(f"Time taken: {str(end - start)} seconds")
