
def main():
    lst = []
    for p in range(20,1000):
        print(p)
        lst.append((p,result(p)))
    lst = sorted(lst, key=lambda x: x[1])
    print(lst[-1])

def result(p):
    t = 0
    for s1 in range(1,p):
        for s2 in range(1,p):
            if s1 + s2 < p:
                s3 = p - (s1 + s2)
                if ((s1*s1) + (s2*s2) == (s3*s3)):
                    t+=1
            else:
                break
    return t

if __name__ == '__main__':
    main()
