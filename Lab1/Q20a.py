# Representation of the graph using a dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

print("Graph representation as a dictionary:")
for node, neighbors in graph.items():
    print(f"{node}: {neighbors}")
