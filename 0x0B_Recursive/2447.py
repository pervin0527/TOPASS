def func(n, x, y):
    if n == 1:
        board[x][y] = '*'
        return
    div = n // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:  # 가운데는 비워둠
                continue
            func(div, x + div * i, y + div * j)

if __name__ == "__main__":
    n = int(input())
    board = [[' ' for _ in range(n)] for _ in range(n)]  # 2차원 리스트를 공백으로 초기화

    func(n, 0, 0)
    for row in board:
        print(''.join(row))
