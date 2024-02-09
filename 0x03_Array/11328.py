"""
https://www.acmicpc.net/problem/11328
"""
import sys

n = int(input())
for _ in range(n):
    str1, str2 = sys.stdin.readline().rstrip().split()

    str1 = sorted(str1)
    str2 = sorted(str2)
    print("Possible" if str1 == str2 else "Impossible")



## 왜 이렇게 어렵게 풀려고 햇을까??....
    # checker = {x : 1 for x in str1}

    # for s in str2:
    #     if s not in checker:
    #         checker[s] = 1
    #     else:
    #         checker[s] -= 1

    # if all(x == 0 for x in checker.values()):
    #     print("Possible")
    # else:
    #     print("Impossible")