import sys
from collections import deque

sys.stdin = open('./txt/problem_32.txt', 'rt')


def DFS(graph, start, visited):
    visited.append(start)
    for adj_index in graph[start]:
        if adj_index not in visited:
            DFS(graph, adj_index, visited)
    return visited


def bfs(graph, v):
    visited = []
    queue = deque([v])
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            for adjacent_node in graph[n]:
                queue.append(adjacent_node)
    return visited



N, M, V = map(int, input().split())
graph = [[] for i in range(N + 1)]
for i in range(M):
    inx, value = list(map(int, input().split()))
    graph[inx].append(value)
    graph[value].append(inx)

visited = []
print(*DFS(graph, V, visited))
print(*bfs(graph, V))

''' 문제 이해하기
1. BFS와 DFS로 출력하는 프로그램을 작성
2. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
   더 이상 방문할 수 없는 경우 종료
3. N : 정점의 개수
4. M : 간선의 개수
5. V : 탐색을 시작할 정점의 번호 V
   그 다음 줄에는 간선이 연결하는 두 정점의 번호
'''
