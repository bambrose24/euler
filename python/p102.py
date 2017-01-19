

def main():
    f = open('p102_triangles.txt')
    ls = f.readlines()
    c = 0
    for l in ls:
        x1,y1,x2,y2,x3,y3 = list(map(int,l.strip().split(',')))
        f1 = getf(x1,y1,x2,y2)
        f2 = getf(x1,y1,x3,y3)
        f3 = getf(x2,y2,x3,y3)
        s = set()
        z1,z2,z3 = f1(0),f2(2),f3(0)
        if (z1 < 0 or z2 < 0 or z3 < 0) and (z1 > 0 or z2 > 0 or z3 > 0):
            c+=1
    print(c)


def getf(x1,y1,x2,y2):
    if x1 == x2:
        return lambda x: 0
    m = (y2-y1)/(x2-x1)
    return lambda x: (m*(x-x1))+y1

if __name__ == '__main__':
    main()
