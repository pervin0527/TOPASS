import sys
input = sys.stdin.readline

from collections import deque

def solution():
    lines = []
    while True:
        line = input().rstrip()
        lines.append(line)

        if line == '.':
            break

    for line in lines:
        if line == '.':
            break

        stack = []
        pair_ok = True
        for c in line:
            if c == '(' or c == '[':
                stack.append(c)
            
            elif c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    print('no')
                    pair_ok = False
                    break

            elif c == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    print('no')
                    pair_ok = False
                    break

        if not pair_ok:
            continue

        if not stack:
            print('yes')
        else:
            print('no')
                

if __name__ == "__main__":
    solution()