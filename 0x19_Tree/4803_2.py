import sys
input = sys.stdin.readline
from collections import deque

def bfs(tree, start, visited):
    queue = deque([start])
    visited[start] = True
    parent = {start: -1}
    
    while queue:
        node = queue.popleft()
        for neighbor in tree[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                queue.append(neighbor)
            elif parent[node] != neighbor:
                return False
    return True

def solution():
    case_number = 0

    while True:
        num_nodes, num_edges = map(int, input().strip().split())
        if num_nodes == 0 and num_edges == 0:
            break
        
        case_number += 1
        adj_list = [[] for _ in range(num_nodes + 1)]
        
        for _ in range(num_edges):
            u, v = map(int, input().strip().split())
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = [False] * (num_nodes + 1)
        num_trees = 0

        for node in range(1, num_nodes + 1):
            if not visited[node]:
                if bfs(adj_list, node, visited):
                    num_trees += 1

        if num_trees == 0:
            print(f'Case {case_number}: No trees.')
        elif num_trees == 1:
            print(f'Case {case_number}: There is one tree.')
        else:
            print(f'Case {case_number}: A forest of {num_trees} trees.')

if __name__ == "__main__":
    solution()
