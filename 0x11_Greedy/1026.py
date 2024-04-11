import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input().rstrip())
    A = list(map(int, input().rstrip().split()))
    B = list(map(int, input().rstrip().split()))

    A.sort()
    B2 = [[x, False] for x in B]

    pair_list = []
    for a in A:
        max_b = -1
        max_idx = -1
        for i in range(N):
            curr_b, state = B2[i]
            if not state and curr_b >= max_b:
                max_b = curr_b
                max_idx = i
        
        B2[max_idx][1] = True
        pair_list.append(a * max_b)

    print(sum(pair_list))