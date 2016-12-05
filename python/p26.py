from util import multiplicativeOrder as m
from math import gcd

def main():
    res = []
    for d in range(10,1001):
        if gcd(10,d) == 1:
            res.append((d,m(10,d)))
    print(max(res, key=lambda x: x[1]))

if __name__ == '__main__':
    main()
