import sys
input = sys.stdin.readline
from collections import deque

def dfs(node, graph, visited, results):
    """
    재귀적인 dfs의 경우 연결 자체가 제한된 값이므로 종료조건을 명시하지 않아도 된다.
    어차피 for문이 가진 visited[neighbor]이 성립하지 않게 되어 재귀적인 호출 자체가 이루어질 수 없음.
    """
    visited[node] = True
    results.append(node)
    
    for neighbor in sorted(graph[node]):
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, results)


def bfs(node, graph, visited, results):
    q = deque()
    q.append(node)
    visited[node] = True

    while q:
        tmp = q.popleft()
        results.append(tmp)

        for neighbor in sorted(graph[tmp]):
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = True

    return results


def solution1():
    N, M, V = map(int, input().strip().split())
    
    ## 인접리스트 생성
    graph = {i: [] for i in range(1, N+1)}
    for _ in range(M):
        u, v = map(int, input().strip().split())
        graph[u].append(v)
        graph[v].append(u)

    results = []
    is_visited = [False] * (N + 1) ## 방문 체크 리스트
    dfs(V, graph, is_visited, results)
    print(" ".join(map(str, results)))

    is_visited = [False] * (N + 1) ## 방문 체크 리스트
    results = bfs(V, graph, is_visited, [])
    print(" ".join(map(str, results)))


if __name__ == "__main__":
    solution1()