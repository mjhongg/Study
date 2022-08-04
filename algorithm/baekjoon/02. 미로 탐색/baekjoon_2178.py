from collections import deque

N, M = map(int, input().split())
node = M
line = 0
tmp = []
graph = [[0]*node for _ in range(node)]

for i in range(N):
    tmp.append(list(map(int, input())))

for i in range(N):
    for j in range(M):
       if tmp[i][j] == 1:
            line += 1
            graph[i][j] = 1


# 노드 갯수 : node (6)
# 간선 갯수 : line (17)



def bfs(graph, start_node):
    now = 0
    cnt = 0
    visit = [0] * line
    que = deque()

    que.append(start_node)

    while que:
        now = que.pop()

        if visit[now] == 0:
            print('node=', now)
            cnt += 1
            visit[now] = 1

            for k in range(M):
                if graph[now][k] == 1 and visit[k] == 0:
                    que.appendleft(k)
                    #cnt += 1
            
    print(cnt)
    return visit

bfs(graph, 0)