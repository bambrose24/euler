import math
from multiprocessing.pool import ThreadPool

def dG(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors[1:]):
        yield divisor

def main():
    most = 28123
    tp = ThreadPool(50)
    res = tp.map(lambda x: (x,dG(x)), range(most))
    l1 = [(x[0],sum(list(x[1]))) for x in res]
    ab = sorted(set([x[0] for x in list(filter(lambda x: x[1] > x[0], l1))]))
    tot = getVal(ab)
    # for i in reversed(range(12,28123)):
    #     if i % 100 == 0:
    #         print(i)
    #     tot += canSum(i,ab)
    print("total: %d" % tot)

def canSum(x,ab):
    for n in ab:
        if n >= x:
            return x
        if (x-n in ab):
            return 0
    return x

def getVal(ab):
    twosum = set()
    for a in ab:
        twosum = twosum.union(set([x+a for x in ab]))
    return sum(set(range(28123))-twosum)


if __name__ == '__main__':
    main()
