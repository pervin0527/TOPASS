## BOJ - 15688
import sys
from collections import Counter

def solution1():
    table = [0] * 2_000_000
    mid = 1_000_000

    n = int(input())
    for _ in range(n):
        k = int(input())

        idx = mid + k
        table[idx] += 1

    for i in range(len(table)):
        if not table[i]:
            continue

        for _ in range(table[i]):
            print(i - mid)


def solution2():
    table = {}

    n = int(input())
    for _ in range(n):
        k = int(input())
        
        if not k in table:
            table[k] = 1
        else:
            table[k] += 1

    for key in sorted(table.keys()):
        for _ in range(table[key]):
            print(key)


def solution3():
    n = int(sys.stdin.readline().rstrip())
    
    numbers = []
    for _ in range(n):
        numbers.append(int(sys.stdin.readline().rstrip()))
    
    counter = Counter(numbers)
    sorted_numbers = sorted(counter.items())
    
    result = []
    for number, count in sorted_numbers:
        result.extend([str(number)] * count)
    
    sys.stdout.write('\n'.join(result) + '\n')


if __name__ == "__main__":
    # solution1()
    # solution2()
    solution3()