from collections import deque

graph = {
    'A' : ['B', 'F', 'I'],
    'B' : ['C', 'E'],
    'C' : ['B', 'D', 'E'],
    'D' : ['G', 'H'],
    'E' : ['B', 'C', 'G'],
    'F' : ['A', 'G'],
    'G' : ['D', 'E', 'F'],
    'H' : ['D'],
    'I' : ['A']
}

def bfs(graph, start_node):
    visit = deque()
    que = deque(start_node)

    while que:
        node = que.popleft()
        if node not in visit:
            visit.append(node)
            que.extend(graph[node])

    return visit

print(bfs(graph, 'A'))