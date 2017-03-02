from math import log

def main():
    f = open('data/p099_base_exp.txt').readlines()
    d = [[int(y.strip()) for y in x.strip().split(',')] for x in f]
    line = 0
    m = 0
    for i in range(len(f)):
        base,exp = d[i][0],d[i][1]
        line_num = i+1
        value = exp*log(base)
        if value > m:
            m = value
            line = line_num
    print('answer: %d' % line)


if __name__ == '__main__':
    main()
