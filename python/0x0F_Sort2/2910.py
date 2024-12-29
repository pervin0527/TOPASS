import sys

if __name__ == "__main__":
    n, c = map(int, sys.stdin.readline().rstrip().split())
    line = list(map(int, sys.stdin.readline().rstrip().split()))

    rank = 1
    checker = {}
    for num in line:
        if num not in checker:
            checker[num] = [1, rank]  # cnt, rank
            rank += 1
        else:
            checker[num][0] += 1  # cnt 증가

    # cnt 큰 순으로, 그리고 cnt가 같다면 rank 낮은 순으로 정렬
    print(checker.items())
    sorted_nums = sorted(checker.items(), key=lambda x: (-x[1][0], x[1][1]))

    result = []
    for num, (cnt, _) in sorted_nums:
        result.extend([num] * cnt)  # cnt만큼 숫자를 결과 리스트에 추가

    print(' '.join(map(str, result)))
