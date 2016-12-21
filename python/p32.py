from itertools import permutations as perms

def main():
    r = range(1,10)
    ps = perms(r)
    res = set()
    for p in ps:
        s = nums(p)
        res = res.union(s)
    print(sum(res))

def nums(p):
    s = set()
    p = list(p)
    for i in range(1,4):
        m1 = num(p,0,i)
        for j in range(i+1,len(p)-1):
            m2 = num(p,i+1,j)
            m3 = num(p,j+1,len(p)-1)
            if m1*m2 == m3:
                s.add(m3)
                print(m3)
    return s

def num(l,low,high):
    s = ""
    for i in range(low,high+1):
        s+=str(l[i])
    return int(s)

if __name__ == '__main__':
    main()
