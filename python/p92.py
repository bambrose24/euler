
def main():
    r = range(1,10000000)
    # r = range(1,1000000)
    c = 0
    for x in r:
        if x % 100000 == 0:
            print(x)
        res = f(x)
        if res == 89:
            c+=1
    print('answer: %d' % c)

def f(x):
    while x != 89 and x != 1:
        x = sod(x)
    return x

def sod(x):
    # try with str and divided by 10
    tot = 0
    while x > 0:
        residual = x % 10
        tot += residual**2
        x //= 10
    return tot

if __name__ == '__main__':
    main()
