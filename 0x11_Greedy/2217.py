import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input().rstrip())
    ropes = [int(input().rstrip()) for _ in range(N)]
    ropes.sort(reverse=True)
    
    k = 1
    max_weight = ropes[0]
    for i in range(1, N):
        curr_rope = ropes[i]
        k += 1
        curr_weight = curr_rope * k

        if curr_weight > max_weight:
            max_weight = curr_weight
        else:
            continue

    print(max_weight)

    # max_weight = 0
    # for i in range(N):
    #     curr_weight = ropes[i] * (i + 1)
    #     max_weight = max(max_weight, curr_weight)

    # print(max_weight)