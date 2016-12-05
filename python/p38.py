
def main():
    res = set('123456789')
    m = 0
    for i in range(int(1e6)):
        s = ''
        j = 1
        while len(s+str(i*j)) < 10:
            s += str(i*j)
            j+=1
        if set(s) == res and int(s) > m:
            m = int(s)
    print(m)

if __name__ == '__main__':
    main()
