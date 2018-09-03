
def main():
    matrix = get_matrix()
    scores = [[0 for i in range(80)] for j in range(80)]

    score_matrix = get_score_matrix(matrix, scores)
    print(score_matrix[79][79])

def get_score_matrix(data, scores):
    for y in range(80):
        for x in range(80):
            scores[x][y] = min_score(data, scores, x, y)
    return scores

def min_score(data, scores, x, y):
    if x == 0:
        if y == 0:
            return data[0][0]
        else:
            return scores[x][y-1] + data[x][y]
    else:
        if y == 0:
            return scores[x-1][y] + data[x][y]
        else:
            c1,c2 = scores[x-1][y], scores[x][y-1]
            return min(c1,c2) + data[x][y]
    return 0


def get_matrix():
    f = open('p081_matrix.txt')
    lines = f.readlines()
    return [[int(x) for x in l.split(',')] for l in lines]

if __name__ == '__main__':
    main()
