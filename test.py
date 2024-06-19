import sys
input = sys.stdin.readline

def solution1():
    n = int(input())
    if n <= 3:
        print(1)

    else:
        table = [0] * 1000000
        table[0] = n

        for i in range(1, len(table)):
            if table[i-1] % 3 == 0:
                table[i] = table[i-1] // 3
            elif table[i-1] % 2 == 0:
                table[i] = table[i-1] // 2
            else:
                table[i] = table[i-1] - 1

            if table[i] == 1:
                print(i-1)
                break


def solution2():
    n = int(input())
    table = [0] * (n+1)

    for i in range(2, n+1):
        table[i] = table[i-1] + 1

        if i % 2 == 0:
            table[i] = min(table[i], table[i//2] + 1)

        if i % 3 == 0:
            table[i] = min(table[i], table[i//3] + 1)

    print(table[n])


if __name__ == "__main__":
    solution2()