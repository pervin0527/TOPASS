import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    table = [0] * 2000001 ## 0은 1000000이며, 이보다 작으면 음수고 크면 양수.

    for _ in range(n):
        value = int(sys.stdin.readline().rstrip())
        table[value + 1000000] += 1 ## -1이면 99999가 되고, 1이면 1000001이 된다.

    output = []
    for i in range(len(table)):
        if table[i] > 0:
            output.extend([str(i - 1000000)] * table[i])
    
    sys.stdout.write('\n'.join(output))