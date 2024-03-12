import sys

# 빠른 입력을 위한 설정
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input().strip())
    nums = [int(input().strip()) for _ in range(n)]

    # 내장 정렬 함수 사용
    nums.sort()

    # 결과를 한 번에 출력하기 위해 문자열로 변환
    print('\n'.join(map(str, nums)))
