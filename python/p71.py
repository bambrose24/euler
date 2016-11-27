from fractions import Fraction as F

def main():
    f = F(3,7)
    best = F(1,100)
    m = 1000000
    s = set()
    for a in range(11,m+1):
        b = int((7/3) * a) - 10
        if b <= m:
            fxs = [F(a,b+i) for i in range(20)]
            for fx in fxs:
                if fx < f and fx > best and fx.denominator <= m:
                    best = fx
    print(best)

if __name__ == '__main__':
    main()
