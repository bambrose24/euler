
def main():
    l = list(filter(lambda x: x > 9 and (x % 10 != 0), range(100)))
    nums = []
    denoms = []
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] < l[j] and l[i] % 11 != 0 and l[j] % 11 != 0:
                os = set(list([l[i]//10, l[i]%10]))
                ts = set(list([l[j]//10, l[j]%10]))
                real = l[i]/l[j]
                if len(os.intersection(ts)) == 1:
                    res = list(os - ts)[0]/list(ts - os)[0]
                    if res == real:
                        nums.append(l[i])
                        denoms.append(l[j])
    print(nums, denoms)

if __name__ == '__main__':
    main()
