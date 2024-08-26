import sys

def solution():
    k = int(sys.stdin.readline().rstrip())

    values = []
    for _ in range(k):
        values.append(int(sys.stdin.readline().rstrip()))
    
    stack = []
    for value in values:
        if value == 0:
            stack.pop()
        else:
            stack.append(value)

    print(sum(stack))
        

if __name__ == "__main__":
    solution()