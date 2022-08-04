from collections import deque

# 인접행렬로 풀기

N, M, V = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
visit = [0] *(N+1)


for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


def dfs(graph, start_node):
    stack = deque()
    stack.append(start_node)

    while stack:
        node = stack.pop()
        if visit[node] == 0 :
            print(node, end=' ')
            visit[node] = 1

            for j in range(N, -1, -1):
                if visit[j] == 0 and graph[node][j] == 1:
                    stack.append(j)
                
    return visit

def bfs(graph, start_node):
    visit = [0] *(N+1)
    que = deque()
    que.append(start_node)

    while que:
        node = que.pop()
        if visit[node] == 0 :
            print(node, end=' ')
            visit[node] = 1

            for j in range(N+1):
                if visit[j] == 0 and graph[node][j] == 1:
                    que.appendleft(j)
    return visit


dfs(graph, V)
print()
bfs(graph, V)