def func_recursive(tmp, a_idx, b_idx):
    if tmp == N+M:
        return
    
    if a_idx >= N: ## A에 더 이상 원소가 없을 경우
        result[tmp] = B[b_idx]
        func_recursive(tmp+1, a_idx, b_idx+1)
    
    elif b_idx >= M or A[a_idx] <= B[b_idx]: ## B에 더 이상 원소가 없을 경우.
        result[tmp] = A[a_idx]
        func_recursive(tmp+1, a_idx+1, b_idx)
    
    else:
        result[tmp] = B[b_idx]
        func_recursive(tmp+1, a_idx, b_idx+1)


def func_iter(a, b):
    a_idx, b_idx = 0, 0
    for i in range(N+M):
        if a_idx >= N:
            result[i] = b[b_idx]
            b_idx += 1

        elif b_idx >= M or a[a_idx] <= b[b_idx]:
            result[i] = a[a_idx]
            a_idx += 1

        else:
            result[i] = b[b_idx]
            b_idx += 1


if __name__ == "__main__":
    N, M = map(int, input().split()) ## A의 크기, B의 크기

    ## A와 B는 이미 정렬되어 있다.
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = [0] * (N+M)
    # func_recursive(0, 0, 0)
    func_iter(A, B)
    print(" ".join([str(x) for x in result]))