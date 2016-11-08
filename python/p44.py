
def main():
    print(solve(10000))

def solve(n):
    p = pents(n)
    ps = set(p)
    m = max(p)*2
    for i in range(len(p)-2):
        for j in range(i+1,len(p)-1):
            p1 = p[i]
            p2 = p[j]
            if (p2+p1) in ps and (p2-p1) in ps:
                m = min(abs(p1-p2), m)
    return m


def pents(n):
    return [(i * ((3*i) - 1)) // 2 for i in range(1,n+1)]

if __name__ == '__main__':
    main()
