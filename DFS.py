matrix = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0]
]
n = len(matrix)
visited = []

def dfs(node):
    visited.append(node)
    for j in range(n):
        if matrix[node][j] == 1 and j not in visited:
            dfs(j)

print("Adjacency Matrix:")
for row in matrix:
    print(row)
dfs(0)
print("DFS traversal from 0:", visited)