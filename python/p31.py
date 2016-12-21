amount = 200
denoms = [1,2,5,10,20,50,100,200]
table = [[0 for i in range(amount+1)] for d in denoms]
for i in range(amount+1):
    table[0][i] = 1
for i in range(len(denoms)):
    table[i][0] = 1

def main():
    for r in range(1,len(denoms)):
        for c in range(1,amount+1):
            table[r][c] = table[r-1][c]
            if c - denoms[r] >= 0:
                table[r][c] += table[r][c-denoms[r]]
    print(table[-1][-1])

if __name__ == '__main__':
    main()
