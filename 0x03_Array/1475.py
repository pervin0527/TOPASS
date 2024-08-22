import sys
import math
input = sys.stdin.readline

# def solution():
#     """
#     문제점 : 입력이 0으로만 구성되었을 때를 처리할 수 없다. 즉, 0을 카운팅할 수 없다.
#     """
#     room_num = int(input())
    
#     p_nums = [0] * 10
#     while room_num > 0:
#         remain = room_num % 10
#         quote = room_num // 10

#         if remain == 6 and p_nums[remain] > 1:
#             p_nums[9] += 1
#         elif remain == 9 and p_nums[remain] > 1:
#             p_nums[6] += 1
#         else:
#             p_nums[remain] += 1

#         room_num = quote

#     print(max(p_nums))


def solution():
    room_num = input().strip()
    
    p_nums = [0] * 10
    for digit in room_num:
        p_nums[int(digit)] += 1
    
    # 6과 9를 합쳐서 필요한 세트를 계산
    six_nine_count = p_nums[6] + p_nums[9]
    p_nums[6] = p_nums[9] = math.ceil(six_nine_count / 2) ## math.ceil : 2.xx 인 경우 3으로 올림.
    
    print(max(p_nums))

if __name__ == "__main__":
    solution()