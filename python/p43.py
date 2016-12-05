from itertools import permutations
# [1,4,0,6,3,5,7,2,8,9]
def main():
    ps = [2,3,5,7,11,13,17]
    lst = list(range(10))
    s = 0
    for p in permutations(lst):
        flag = True
        for i in range(len(ps)):
            t = p[i+1]*100 + p[i+2]*10 + p[i+3]
            if not t % ps[i] == 0:
                flag = False
                break
        if flag:
            x = ""
            for number in p:
                x += str(number)
            s += int(x)
    print(s)

def test(p):
    ps = [2,3,5,7,11,13,17]
    s = 0
    flag = True
    for i in range(len(ps)):
        t = p[i+1]*100 + p[i+2]*10 + p[i+3]
        print(' %d' % t)
        if not t % ps[i] == 0:
            flag = False
            break
    if flag:
        x = ""
        for number in p:
            x += str(number)
        s += int(x)
    return s


if __name__ == '__main__':
    main()
