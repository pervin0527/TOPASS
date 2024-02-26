import sys

def check_matrix(matrix, x, y, size):
    curr = matrix[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if curr != matrix[i][j]:
                return False
    return True

def divide_matrix(matrix, x, y, size):
    if check_matrix(matrix, x, y, size):
        result[matrix[x][y]] += 1

        return

    new_size = size // 2
    for i in range(2):
        for j in range(2):
            divide_matrix(matrix, x+i*new_size, y+j*new_size, new_size)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    paper = []
    result = {0 : 0, 1: 0}
    for _ in range(n):
        paper.append(list(map(int, sys.stdin.readline().rstrip().split())))

    divide_matrix(paper, 0, 0, n)
    for r in list(result.values()):
        print(r)