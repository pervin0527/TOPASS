if __name__ == "__main__":
    n = int(input())
    colors = [list(map(int, input().split())) for _ in range(n)] ## [[R, G, B], ...]
    table = [[0, 0, 0] for _ in range(n)]

    ## initial values
    table[0][0] = colors[0][0]
    table[0][1] = colors[0][1]
    table[0][2] = colors[0][2]

    for i in range(1, n):
        table[i][0] = min(table[i-1][1], table[i-1][2]) + colors[i][0]
        table[i][1] = min(table[i-1][0], table[i-1][2]) + colors[i][1]
        table[i][2] = min(table[i-1][0], table[i-1][1]) + colors[i][2]

    print(min(table[n-1]))