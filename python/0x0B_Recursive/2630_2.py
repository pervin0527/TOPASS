def same_check(matrix, row, col, size):
    curr = matrix[row][col]
    for x in range(row, row + size):
        for y in range(col, col + size):
            if curr != matrix[x][y]:
                return False
    return True

def divide_matrix(matrix, row, col, size):
    if same_check(matrix, row, col, size):
        results[matrix[row][col]] += 1
        return
    
    new_size = size // 2
    for x in range(2):
        for y in range(2):
            divide_matrix(matrix, row + new_size * x, col + new_size * y, new_size)


if __name__ == "__main__":
    n = int(input())
    papers = [list(map(int, input().split())) for _ in range(n)]

    results = {0:0, 1:0}
    divide_matrix(papers, 0, 0, n)
    for res in list(results.values()):
        print(res)