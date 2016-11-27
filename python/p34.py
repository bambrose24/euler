from math import factorial as fa

def main():
    low = 100000
    r = range(low,100*low)
    facts = {str(x):fa(x) for x in range(10)}
    count = 0
    res = [145, 40585]
    for i in r:
        st = str(i)
        s = sum([facts[x] for x in st])
        if s == i:
            count+=1
            res.append(i)
    print(res)
    print(sum(res))

if __name__ == '__main__':
    main()
