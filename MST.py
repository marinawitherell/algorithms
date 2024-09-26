import heapq

def Prims(G):
    n = len(G)
    visited = set()
    mst = []
    pq = [(0, 0, 0)]  # (weight, parent, vertex)
    
    while pq:
        weight, parent, vertex = heapq.heappop(pq)
        if vertex not in visited:
            visited.add(vertex)
            if parent != vertex:  # Avoid adding the initial dummy edge
                mst.append((parent, vertex, weight))
            for neighbor, weight in enumerate(G[vertex]):
                if weight != 0 and neighbor not in visited:
                    heapq.heappush(pq, (weight, vertex, neighbor))
    
    return mst

