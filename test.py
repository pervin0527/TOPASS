import sys
input = sys.stdin.readline

def solution1():
    n = int(input())
    meetings = []
    for _ in range(n):
        start, end = map(int, input().split())
        meetings.append((start, end))

    # 회의 리스트를 끝나는 시간, 시작 시간 순으로 정렬합니다.
    meetings.sort(key=lambda x: (x[1], x[0]))

    count = 0
    last_end_time = 0

    for start, end in meetings:
        if start >= last_end_time:
            count += 1
            last_end_time = end
    
    print(count)

if __name__ == "__main__":
    solution1()
