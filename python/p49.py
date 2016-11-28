import util as u

def main():
    ps = u.primesUpTo(10000)
    ps = list(filter(lambda x: x > 999, ps))
    pss = set(ps)
    res = []
    for i in range(len(ps)):
        j = 0
        while j < i:
            low,mid = ps[j],ps[i]
            s1,s2 = set(str(low)), set(str(mid))
            dif = mid-low
            s3 = set(str(dif+mid))
            if mid+dif in pss and s1 == s2 and s2 == s3 and s1 == s3:
                res.append((low,mid,mid+dif))
            j+=1
    res = sorted(res)
    print(res)

if __name__ == '__main__':
    main()
