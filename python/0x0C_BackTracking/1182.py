"""
크기가 양수인(공집합을 제외한 최소 하나 이상의 원소를 갖는) 부분집합에서, 원소들의 총합이 s와 같은 경우의 수를 구해라.
"""

n, s = map(int, input().split())  # 정수의 개수 N과 합 S를 입력받음
arr = list(map(int, input().split()))  # N개의 정수를 입력받아 리스트에 저장
cnt = 0  # 합이 S가 되는 부분수열의 개수를 카운트하는 변수

def func(cur, tot):
    """
    cur은 매 단계, tot는 부분 집합을 구성하는 원소들의 총 합.
    """
    global cnt  # 전역 변수 cnt를 사용하겠다고 선언
    if cur == n:  # 모든 원소를 고려했다면
        if tot == s:  # 현재까지의 합이 S와 같다면
            cnt += 1
        return
    func(cur + 1, tot)  # 현재 원소를 포함하지 않는 경우
    func(cur + 1, tot + arr[cur])  # 현재 원소를 포함하는 경우

func(0, 0)  # 초기 호출
if s == 0: 
    cnt -= 1  # 공집합을 제외하기 위해 S가 0일 때는 카운트를 하나 줄임
print(cnt)  # 최종 카운트된 값을 출력
