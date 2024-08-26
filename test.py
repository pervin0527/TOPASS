import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

    i = 1
    stack = []
    result = []
    state = True
    for a in arr:
        while i <= a:
            stack.append(i)
            result.append("+")
            i += 1

        if stack[-1] == a:
            stack.pop()
            result.append("-")
        else:
            state = False
            print("NO")
            break

    if state:
        for r in result:
            print(r)

if __name__ == "__main__":
    solution()