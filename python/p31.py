
# NOTE NOT DONE

amount = 200
denoms = [1,2,5,10,20,50,100,200]
table = [[0 for i in range(amount+1)] for d in range(len(denoms)+1)]

def main():
    for i in range(len(denoms)):
        table[i][0] = 1
    for j in range(1,amount+1):
        table[0][j] = 0

    for i in range(1,len(denoms)+1):
        for j in range(1,amount+1):
            table[i][j] = table[i-1][j]
            if denoms[i-1] <= j:
                table[i][j] += table[i-1][j] + table[i][j - denoms[i-1]]


    print(table[len(denoms)][amount])

if __name__ == '__main__':
    main()
