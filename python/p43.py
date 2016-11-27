from itertools import permutations

def main():
    ps = [2,3,5,7,11,13,17]
    lst = list(range(10))
    s = 0
    for p in permutations(lst):
        flag = True
        for i in range(len(ps)):
            t = p[i]*100 + p[i]*10 + p[i]
            if not t % ps[i] == 0:
                flag = False
        if flag:
            n = reduce(lambda x,y: str(x)+str(y), p)
            n = int(n)
            s += n
    print(s)

if __name__ == '__main__':
    main()
