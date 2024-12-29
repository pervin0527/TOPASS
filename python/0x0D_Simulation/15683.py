import copy

def dfs(arr, ds, x, y):
    for d in ds: ## [0, 2]를 순서대로 탐색함.
        cx, cy = x, y
        while True:
            cx += dx[d]
            cy += dy[d]

            if cx < 0 or cy < 0 or cx >= n or cy >= m:
                break
            if arr[cx][cy] == 6:
                break
            elif arr[cx][cy] == 0:
                arr[cx][cy] = 7


def backtrack(tmp, matrix):
    global min_val
    if tmp == len(cameras):
        n_zeros = 0
        for i in range(n):
            n_zeros += matrix[i].count(0)
        min_val = min(n_zeros, min_val)
        return
    
    cam_type, x, y = cameras[tmp]
    tmp_matrix = copy.deepcopy(matrix)
    
    ## 카메라의 설정값 하나가 선택. -> dfs로 탐색 범위(직선)을 모두 확인 -> 재귀 -> 원래 상태로 되돌아옴.
    ## 위 구조가 순환되면서 1번 카메라의 각도가 바뀌었을 때, 다른 카메라의 설정도 탐색.
    for direction in directions[cam_type]: ## 카메라가 2번이면 direction = [0, 2]
        dfs(tmp_matrix, direction, x, y)
        backtrack(tmp+1, tmp_matrix)
        tmp_matrix = copy.deepcopy(matrix)
        

if __name__ == "__main__":
    n, m = map(int, input().split())

    graph = []
    cameras = [] ## cam_type, x, y
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
        for j in range(m):
            if row[j] in [1, 2, 3, 4, 5]:
                cameras.append((row[j], i, j)) ## 1~5 카메라 유형이 i행 j열 원소임을 저장.
    
    ## 동 -> 북 -> 서 -> 남
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    ## dx, dy의 설정에 따라 카메라의 각도를 설정해야함.(매우 중요)
    directions = [
        [],
        [[0], [1], [2], [3]],
        [[0, 2], [1, 3]],
        [[0, 3], [0, 1], [1, 2], [2, 3]],
        [[0, 2, 3], [0, 1, 3], [0, 1, 2], [1, 2, 3]],
        [[0, 1, 2, 3]]
    ]

    min_val = int(1e9)
    backtrack(0, graph)
    print(min_val)