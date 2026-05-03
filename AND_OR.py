graph = {
    'A': [[('B', 1), ('C', 1)],[('D', 1)]],
    'B': [[('G', 1)]],
    'D': [[('E', 1), ('F', 1)]]
}

h = {
    'A': 3,
    'B': 9,
    'C': 16,
    'D': 12,
    'E': 5,
    'F': 5,
    'G': 7
}


def ao_star(n):
    print("Expanding node:", n)
    if n in graph:
        min_cost = float('inf')
        best_path = None

        for path in graph[n]:
            cost = sum(h[node] + weight for node, weight in path)
            if cost < min_cost:
                min_cost = cost
                best_path = path

        h[n] = min_cost
        for node, weight in best_path:
            ao_star(node)

ao_star('A')
print("\nUpdated heuristic values:", h  )