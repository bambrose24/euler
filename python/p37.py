from time import time
import util

def main():
    MAX = 1000000
    start = time()
    print('primes up to...')
    primes = util.primesUpTo(MAX)
    print(' done')
    ps = set(primes)
    res = []
    print('loop...')
    for i in range(len(primes)):
        p = primes[i]
        s = set([p])
        lp = p
        while lp > 0:
            lp = lp // 10
            s.add(lp)
        rp = p
        while rp > 0:
            st = str(rp)[1:]
            if st != '':
                rp = int(st)
                s.add(rp)
            else:
                rp = 0
        s = s - set([0])
        if len(s) == len(s.intersection(ps)):
            res.append(p)
    res = list(filter(lambda x: x > 10, res))
    print('answer: %d' % sum(res))




if __name__ == '__main__':
    main()
