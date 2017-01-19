# NOT DONE

def main():
    flag = False
    i = 1
    while not flag:
        if test(i,6):
            flag = True
        else:
            i+=1
    print('answer: %d' % i)

def test(x,i):
    lst = [set(str(x*y)) for y in range(1,i+1)]
    res = lst[0]
    for y in range(1,len(lst)):
        res = res.union(lst[y])
    return lst[0] == res

if __name__ == '__main__':
    main()
