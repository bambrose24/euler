import numpy as np
import util as u
from itertools import permutations as p

def main():
    lst = []
    for i in range(3,10):
        lst += p(list(range(1,i)))
    lst = list(map(flatten, lst))
    lst = list(filter(u.isPrime, lst))
    print(max(lst))

def flatten(x):
    return int(str(x).replace('(','').replace(')','').replace(',','').replace(' ',''))


if __name__ == '__main__':
    main()
