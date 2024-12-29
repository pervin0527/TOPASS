import sys
import math
input = sys.stdin.readline

# def solution():
#     n, k = map(int, input().strip().split())

#     rooms = {}
#     for i in range(1, 7):
#         rooms[f"{i}_0"] = []
#         rooms[f"{i}_1"] = []

#     for _ in range(n):
#         s, y = map(int, input().strip().split())
#         rooms[f"{y}_{s}"].append(1)

#     count = 0
#     for i in range(1, 7):
#         if 0 < len(rooms[f"{i}_0"]) <= k:
#             count += 1
#         else:
#             count += math.ceil(len(rooms[f"{i}_0"]) / k)

#         if 0 < len(rooms[f"{i}_1"]) <= k:
#             count += 1
#         else:
#             count += math.ceil(len(rooms[f"{i}_1"]) / k)

#     print(count)

def solution():
    n, k = map(int, input().strip().split())

    # 학년별, 성별로 학생 수를 카운트할 2차원 리스트 초기화
    students = [[0] * 2 for _ in range(7)]

    # 학생 정보를 입력받아 카운트
    for _ in range(n):
        s, y = map(int, input().strip().split())
        students[y][s] += 1

    # 필요한 방의 수 계산
    count = 0
    for i in range(1, 7):
        for j in range(2):
            if students[i][j] > 0:
                count += math.ceil(students[i][j] / k)

    print(count)

    
if __name__ == "__main__":
    solution()