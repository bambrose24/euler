import fractions

def phi(n):
    amount = 0

    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1

    return amount

def main():
    m = 0
    n = 0
    r = range(2,10)
    r = range(5,1000001)
    r = range(5,1001)
    for i in r:
        res = i / phi(i)
        if res > m:
            m = res
            n = i
    print('answer: %d' % n)

if __name__ == '__main__':
    main()
