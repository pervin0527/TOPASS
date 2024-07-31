import sys
input = sys.stdin.readline
from collections import deque

def solution():
    ## N : 학생 수
    ## M : 키를 비교한 결과 수(=간선의 수)
    N, M = map(int, input().strip().split())
    
    adj_list = [[] for _ in range(N + 1)]
    indeg_list = [0] * (N + 1) ## 각 정점별 Indegree를 측정한 리스트.
    for _ in range(M):
        u, v = map(int, input().strip().split())
        adj_list[u].append(v) ## 방향 그래프이므로 단방향 간선.
        indeg_list[v] += 1

    # print(adj_list)
    # print(indeg_list)

    ## 들어오는 간선이 없는 정점들을 큐에 추가.
    queue = deque()
    for idx in range(1, len(indeg_list)):
        if indeg_list[idx] == 0:
            queue.append(idx) ## idx번째 정점을 큐에 추가.

    result = []
    while queue:
        node = queue.popleft()
        result.append(node)

        connects = adj_list[node] ## 현재의 정점에서 나가는 간선들로 연결된 정점들
        for conn in connects:
            indeg_list[conn] -= 1

            if indeg_list[conn] == 0:
                queue.append(conn)

    result = map(str, result)
    print(' '.join(result))

if __name__ == "__main__":
    solution()