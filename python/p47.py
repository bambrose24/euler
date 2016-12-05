from util import factors as f

def main():
    c = 10
    fs = 4
    table = {}
    table[c-1] = set(f(c-1))
    table[c-2] = set(f(c-2))
    table[c-3] = set(f(c-3))
    while 1:
        print(c)
        if not c in table:
            table[c] = set(f(c))
        s1,s2,s3,s4 = table[c],table[c-1],table[c-2],table[c-3]
        if len(s1)==fs and len(s2)==fs and len(s3)==fs and len(s4)==fs:
            print(c-3)
            break
        c+=1

if __name__ == '__main__':
    main()
