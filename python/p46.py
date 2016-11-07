import numpy as np

def main():
    m = 1000000
    ps = primesfrom2to(m)
    sq = np.array([2*(x*x) for x in range(m)])
    pss = set(ps)
    sqs = set(sq)

    print("answer: %d" % findNum(pss,sqs,m))

def findNum(pss,sqs,m):
    for odd in range(3,m,2):
        print(odd)
        if odd not in pss:
            flag = False
            for sq in sqs:
                if (odd-sq) in pss:
                    flag = True
                    break
            if not flag:
                return odd

def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in range((int(n**0.5)//3)+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

if __name__ == '__main__':
    main()
