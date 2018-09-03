from fractions import gcd

def main():
    L = 1500000
    L = 1500
    nums = [0 for i in range(L+1)]
    lst = get_lst(L)
    print(len(lst))
    for s,t in lst:
        a = s*t
        b = ((s*s)-(t*t))//2
        c = ((s*s)+(t*t))//2
        perim = a+b+c
        i = 1
        while perim*i < len(nums):
            nums[perim*i]+=1
            i+=1
    count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count+=1
    print('answer: %d' % count)

def get_lst(L):
    lst = []
    for i in range(3,L,2):
        for j in range(i+2,L,2):
            if gcd(i,j) == 1:
                lst.append((j,i))
    return lst

if __name__ == '__main__':
    main()
