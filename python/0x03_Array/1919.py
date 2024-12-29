import sys
input = sys.stdin.readline
from collections import Counter

def solution():
    s1 = input().strip()
    s2 = input().strip()

    # 각 단어에서 문자 빈도수를 계산
    counter1 = Counter(s1) ## Counter({'a': 2, 'b': 2, 'c': 2})
    counter2 = Counter(s2) ## Counter({'x': 2, 'y': 2, 'b': 2})

    # 두 Counter 객체 간의 차이 계산
    diff1 = (counter1 - counter2) ## Counter({'a': 2, 'c': 2})
    diff2 = (counter2 - counter1) ## Counter({'x': 2, 'y': 2})
    diff_counter = diff1 + diff2

    # 차이의 총합이 제거해야 할 문자 수
    print(sum(diff_counter.values()))

# def solution():
#     s1 = input().strip()
#     s2 = input().strip()

#     arr = [0] * 26
#     for i in range(len(s1)):
#         idx = ord(s1[i]) - 97
#         arr[idx] += 1

#     for i in range(len(s2)):
#         idx = ord(s2[i]) - 97
#         arr[idx] -= 1

#     count = 0
#     for i in arr:
#         count += abs(i)

#     print(count)

        
if __name__ == "__main__":
    solution()