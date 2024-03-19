if __name__ == "__main__":
    t = int(input())
    table = [0] * 11
    
    table[1], table[2], table[3] = 1, 2, 4
    for i in range(4, 11):
        table[i] = table[i-1] + table[i-2] + table[i-3]

    while t > 0:
        n = int(input())
        print(table[n])
        t -= 1