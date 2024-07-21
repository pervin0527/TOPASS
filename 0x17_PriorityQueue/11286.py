import sys
import heapq
input = sys.stdin.readline

def solution1():
    N = int(input().strip())
    numbers = [int(input().strip()) for _ in range(N)]

    heap = []
    for number in numbers:
        if number == 0:
            if len(heap) == 0:
                print(0)
            else:
                root = heapq.heappop(heap)
                print(root[1])
        else:
            ## 우선순위인 abs(number)가 동일한 경우 abs(-1), abs(1) number의 값이 작은 값이 더 높은 우선순위를 갖게 된다.
            heapq.heappush(heap, (abs(number), number))

if __name__ == "__main__":
    solution1()