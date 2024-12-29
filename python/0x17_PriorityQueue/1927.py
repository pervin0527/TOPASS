import sys
import heapq
input = sys.stdin.readline

def solution1():
    N = int(input().strip())
    numbers = [int(input().strip()) for _ in range(N)]

    heap = []
    for number in numbers:
        if number == 0:
            if len(heap) > 0:
                value = heapq.heappop(heap)
                print(value)
            else:
                print(0)
        
        else:
            heapq.heappush(heap, number)

if __name__ == "__main__":
    solution1()