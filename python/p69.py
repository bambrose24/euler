from util import *

def main():
    m = 0
    n = 0
    r = range(2,10)
    r = range(5,1000001)
    r = range(5,1001)
    for i in r:
        if i % 100 == 0:
            print(i)
        x = phi(i)
    print('answer: %d' % n)

if __name__ == '__main__':
    main()
