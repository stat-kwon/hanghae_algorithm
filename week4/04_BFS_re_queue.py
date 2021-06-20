
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}


def bfs_queue(graph, start):
    queue = [start]
    visited = []
    while queue:
        current_node = queue.pop(0)
        visited.append(current_node)
        for adjacent_node in graph[current_node]:
            if adjacent_node not in visited:
                queue.append(adjacent_node)
    return visited

print(bfs_queue(graph, 1))