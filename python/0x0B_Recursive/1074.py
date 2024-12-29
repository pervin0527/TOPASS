"""
초기 조건
  - n = 2, r = 3, c = 1
  - half = 2 ** (2-1) = 2

첫 번째 호출 func(2, 3, 1)
  - half = 2
  - r >= half와 c < half 조건을 만족 (3 >= 2 및 1 < 2) → 세 번째 사분면
  - 결과는 2 * half * half + func(n-1, r-half, c)가 됩니다.
  - 2 * 2 * 2 + func(1, 1, 1) → 8 + func(1, 1, 1)

두 번째 호출 func(1, 1, 1)
  - half = 2 ** (1-1) = 1
  - r >= half와 c >= half 조건을 만족 (1 >= 1 및 1 >= 1) → 네 번째 사분면
  - 결과는 3 * half * half + func(n-1, r-half, c-half)가 됩니다.
  - 3 * 1 * 1 + func(0, 0, 0) → 3 + func(0, 0, 0)

세 번째 호출 func(0, 0, 0)
  - n == 0 조건에 도달, 함수는 0을 반환합니다.

최종 결과 계산
  - 두 번째 호출에서의 결과는 3 + 0이므로 3.
  - 첫 번째 호출에서의 결과는 8 + 3이므로 11.
  - 최종적으로, 함수는 11을 반환합니다.
"""

def func(n, r, c):
    if n == 0:
        return 0
    
    """
    2^n의 행렬을 4등분으로 나눴고, r, c가 속하는 사분면을 하나 정해 재귀로 파고듬.
    """
    half = 2 ** (n-1)
    if r < half and c < half:
        return func(n-1, r, c)
    
    if r < half and c >= half:
        """
        half * half : 몇번째 사분면에 있는지에 대한 offset. r, c가 2사분면에 속하는 경우 1사분면에 있는 2^(n-1)개의 칸을 모두 지나갔으므로 그만큼 더하는 것.
        c-half : 2사분면의 시작점은 c - half
        """
        return half * half + func(n-1, r, c-half)
    
    if r >= half and c < half:
        return 2 * half * half + func(n-1, r-half, c)
    
    return 3 * half * half + func(n-1, r-half, c-half)


if __name__ == "__main__":
    n, r, c = map(int, input().split()) ## 2, 3, 1
    print(func(n, r, c))