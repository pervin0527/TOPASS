import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    builds = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

    print()
    count = 0
    stack = []
    for i in range(N-1, -1, -1):
        build = builds[i]

        while stack and build > stack[-1]:
            stack.pop()

        print(len(stack))
        count += len(stack)
        stack.append(build)

    print(count)

if __name__ == "__main__":
    solution()