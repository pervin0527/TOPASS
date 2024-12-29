import sys

def check_same(matrix, x, y, size):
    """주어진 범위의 종이가 모두 같은 수로 되어 있는지 확인하는 함수"""
    start = matrix[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if matrix[i][j] != start:
                return False
    return True

def divide(matrix, x, y, size):
    """종이를 나누고 각각에 대해 재귀적으로 검사하는 함수"""
    if check_same(matrix, x, y, size):
        result[matrix[x][y]] += 1
        return
    
    new_size = size // 3
    for i in range(3):
        for j in range(3):
            divide(matrix, x + i * new_size, y + j * new_size, new_size)


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    paper = []
    result = {-1 : 0, 0 : 0, 1 : 0}
    for _ in range(n):
        row = list(map(int, sys.stdin.readline().rstrip().split()))
        paper.append(row)

    divide(paper, 0, 0, n)
    for r in list(result.values()):
        print(r)