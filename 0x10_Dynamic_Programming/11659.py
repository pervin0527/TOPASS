import sys

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.insert(0, 0)  # 누적 합을 구하기 쉽도록 앞에 0을 추가.

    table = [0] * (n+1)
    table[1] = arr[0]
    for i in range(1, n+1):
        table[i] = table[i-1] + arr[i]

    output = []
    for _ in range(m):
        i, j = map(int, sys.stdin.readline().split())
        output.append(str(table[j] - table[i-1]))

    sys.stdout.write('\n'.join(output))
