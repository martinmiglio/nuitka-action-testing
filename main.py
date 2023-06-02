import time
import math


def calcPi(count):
    pi = sum(math.pow(-1, i) / (2 * i + 1) for i in range(count))
    pi *= 4
    return pi


start = time.time()
pi = calcPi(100000000)
end = time.time()
print(pi)
print(f"Time taken: {str(end - start)} seconds")
