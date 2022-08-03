from collections import deque

# 인접 리스트로 풀기

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, start_node):
    visit = deque()
    adj = deque()

    adj.append(start_node)

    while adj:
        node = adj.pop()

        if node not in visit:
            visit.append(node)
            adj.extend(graph[node])
            print(node, end=' ')

    return visit



def bfs(graph, start_node):
    visit = deque()
    adj = deque()

    adj.append(start_node)

    while adj:
        node = adj.popleft()
        if node not in visit:
            visit.append(node)
            adj.extend(graph[node])
            print(node, end=' ')
        
    return visit


for i in range(N+1):
    graph[i].sort(reverse=True)
dfs(graph, V)

print()

for i in range(N+1):
    graph[i].sort()
bfs(graph, V)







# 인접 행렬로 풀기
'''
graph = [[0]*N for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

print(graph)
'''