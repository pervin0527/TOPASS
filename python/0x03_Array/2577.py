import sys
input = sys.stdin.readline

# def solution():
#     inps = [int(input().strip()) for x in range(3)]
#     abc = inps[0] * inps[1] * inps[2]

#     ## 문자열로 바꿔서 한자리씩 카운팅할 수 있음.
#     check = [0] * 10
#     for c in str(abc):
#         check[int(c)] += 1

#     result = '\n'.join(map(str, check))        
#     print(result)

def solution():
    inps = [int(input().strip()) for _ in range(3)]
    abc = inps[0] * inps[1] * inps[2]

    ## 문자열로 바꾸지 않고 한자리씩 카운팅할 수 있음.
    check = [0] * 10
    while abc > 0:
        digit = abc % 10
        check[digit] += 1
        abc //= 10

    result = '\n'.join(map(str, check))        
    print(result)


if __name__ == "__main__":
    solution()