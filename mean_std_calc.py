'''
This code first generates a list of random numbers using random.gauss(10, 1)
with mean 10 and standard deviation 1;
Then, calculates mean, standard deviation using the formulas. 
Finally, returns the calculated mean and standard deviation.
'''

import random
import math

cycles = 100000

def stats():
    rnd_seq = [random.gauss(10, 1) for i in range(cycles)]

    # Calculate mean
    avg = sum(rnd_seq) / len(rnd_seq)

    # Calculate standard deviation
    squared_diff = [(x - avg) ** 2 for x in rnd_seq]
    std = math.sqrt(sum(squared_diff) / (len(rnd_seq) - 1))

    return avg, std 

if __name__ == '__main__':
    avg, std = stats()
    print(f"{avg:.0f} {std:.0f}") #formats mean, standard deviation as integers & print separated by a space







