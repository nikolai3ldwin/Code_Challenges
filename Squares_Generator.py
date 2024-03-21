'''
The squares() function that acts as a python generator;
The squares() function generates a continuous sequence of the squares of the n integers:
0, 1, 4, 9, 16, ..., n-1 for the parameter n passed to the squares_caller() function.
'''

def squares():
    n = 0
    while True:
        yield n * n
        n += 1

def squares_caller(n):          
    squares_seq = squares()

    for i in range(n):
        print(next(squares_seq))

if __name__ == '__main__':
    n = int(input())
    squares_caller(n)
