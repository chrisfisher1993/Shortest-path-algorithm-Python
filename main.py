# Define a directed graph using an adjacency list representation
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

# Define a function to find the shortest path in the graph from start to target
def shortest_path(graph, start, target=''):
    # Initialize unvisited nodes, distances, and paths dictionaries
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)

    # Iterate until all nodes are visited
    while unvisited:
        # Select the unvisited node with the minimum distance
        current = min(unvisited, key=distances.get)
        
        # Update distances and paths for neighboring nodes
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                # Copy the path if the last node is the current node
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        
        # Mark the current node as visited
        unvisited.remove(current)

    # Determine the list of targets to print based on the provided target parameter
    targets_to_print = [target] if target else graph

    # Print the shortest paths and distances for each target node
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')

    # Return the final distances and paths dictionaries
    return distances, paths

# Example usage: Find the shortest path from 'A' to 'F' in the given graph
shortest_path(my_graph, 'A', 'F')
