graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

def bfs(start):
    visited = [start]
    queue = [start]
    while queue:
        node = queue.pop(0)
        for nb in graph[node]:
            if nb not in visited:
                visited.append(nb)
                queue.append(nb)
    return visited

print("Adjacency List:")
for k in graph:
    print(k, "->", graph[k])
print("BFS traversal from 0:", bfs(0))