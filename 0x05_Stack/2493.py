import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    towers = list(map(int, sys.stdin.readline().rstrip().split()))

    stack = []
    results = [0] * n

    for i in range(n):
        while stack and stack[-1][0] < towers[i]:
            stack.pop()
        
        if stack:
            results[i] = stack[-1][1] + 1
        
        stack.append((towers[i], i))
    
    print(' '.join(map(str, results)))

if __name__ == "__main__":
    solution()
