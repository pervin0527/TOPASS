def backtrack(depth, path):
    if depth == M:
        seq = ' '.join(map(str, path))
        if seq not in seen:
            results.append(path[:])
            seen.add(seq)
        return
    
    for i in range(N):
        if not used[i]:
            used[i] = True
            path.append(numbers[i])
            backtrack(depth + 1, path)
            path.pop()
            used[i] = False

if __name__ == "__main__":
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()

    results = []
    seen = set()
    used = [False] * N
    backtrack(0, [])

    for result in sorted(results):
        print(' '.join(map(str, result)))
