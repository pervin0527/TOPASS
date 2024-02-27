def check_matrix(matrix, row, col, size):
    curr = matrix[row][col]
    for x in range(row, row+size):
        for y in range(col, col+size):
            if curr != matrix[x][y]:
                return False
    return True

def divide_matrix(matrix, row, col, size):
    if check_matrix(matrix, row, col, size):
        results.append(str(matrix[row][col]))
        return
    
    new_size = size // 2
    results.append("(")
    for x in range(2):
        for y in range(2):
            divide_matrix(matrix, row + x * new_size, col + y * new_size, new_size)
    results.append(")")

if __name__ == "__main__":
    n = int(input())
    image = []
    results = []

    for _ in range(n):
        row = [int(x) for x in input()]
        image.append(row)

    divide_matrix(image, 0, 0, n)
    results = "".join(results)
    print(results)