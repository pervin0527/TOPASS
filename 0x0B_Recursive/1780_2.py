def same_check(matrix, row, col, size):
    curr = matrix[row][col]
    for x in range(row, row+size):
        for y in range(col, col+size):
            if curr != matrix[x][y]:
                return False
    return True


def divide_matrix(matrix, row, col, size):
    if same_check(matrix, row, col, size):
        results[matrix[row][col]] += 1
        return

    new_size = size // 3 ## 9등분
    for x in range(3): ## 가로 3등분
        for y in range(3): ## 세로 3등분
            """
            9등분으로 만들어진 9개의 블록을 순차적으로 접근해 더 이상 나눠질 수 없을 때까지 9등분.
            그 과정에서 동일한 숫자로 구성된 블록의 수를 계산(same_check)로 검사하여 results(dict)에 기재함.
            """
            divide_matrix(matrix, row + new_size * x, col + new_size * y, new_size)



if __name__ == "__main__":
    n = int(input())
    papers = [list(map(int, input().split())) for _ in range(n)]

    results = {-1:0, 0:0, 1:0}
    divide_matrix(papers, 0, 0, n)
    for res in list(results.values()):
        print(res)