if __name__ == "__main__":
    n = int(input())
    table = [0] * n

    table[0] = 1
    table[1] = 2
    for i in range(2, n):
        table[i] = table[i-1] + table[i-2]

    print(table[n-1] % 10007)