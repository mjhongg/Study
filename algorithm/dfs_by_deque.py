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

def dfs(graph, start_node):
    visit = deque()
    stack = deque(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit


print(dfs(graph, 'A'))