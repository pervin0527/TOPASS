import sys
input = sys.stdin.readline
from collections import deque

def bfs(start, graph, visited):
    q = deque()
    q.append(start)

    while q:
        node = q.popleft()
        ## 현재 노드가 이전에 방문한 적이 없다면
        if not visited[node]:
            visited[node] = True ## 방문 처리

            ## 방문한 적이 없다면 현재 노드와 연결된 노드들을 모두 큐에 추가한다.
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    q.append(neighbor)

def solution1():
    N, M = map(int, input().strip().split())
    
    ## 인접 리스트로 그래프 구축.
    ## 무방향 그래프이기 때문에 각각의 연결은 양방향 연결이다.
    graph = {i: [] for i in range(1, N+1)}
    visited = [False] * (N + 1) ## 방문처리 기록 리스트
    for i in range(M):
        u, v = map(int, input().strip().split())
        graph[u].append(v)
        graph[v].append(u)

    connected_components = 0
    ## 그래프에 존재하는 모든 노드들을 하나씩 순회하면서 방문 여부를 검사한다.
    for i in range(1, N+1):
        if not visited[i]:
            bfs(i, graph, visited)
            connected_components += 1

    print(connected_components)

if __name__ == "__main__":
    solution1()