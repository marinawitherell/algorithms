
def solve_tsp(G):
    num_nodes = len(G)
    visited = [False] * num_nodes
    path = [0]  # Starting from node 0
    visited[0] = True
    
    while len(path) < num_nodes:
        current_node = path[-1]
        min_dist = float('inf')
        nearest_neighbor = None
        
        for neighbor in range(num_nodes):
            if not visited[neighbor] and G[current_node][neighbor] != 0 and G[current_node][neighbor] < min_dist:
                min_dist = G[current_node][neighbor]
                nearest_neighbor = neighbor
                
        if nearest_neighbor is None:  # If no unvisited neighbors found, return to starting node
            path.append(0)
        else:
            path.append(nearest_neighbor)
            visited[nearest_neighbor] = True
    
    # Return to starting node
    path.append(0)
    return path