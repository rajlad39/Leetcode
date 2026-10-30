import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # dist[u][count] stores the minimum distance to reach node u with `count` consecutive identical characters
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        
        start_count = 1
        dist[0][start_count] = 0
        
        # Priority queue stores (distance, u, count)
        pq = [(0, 0, start_count)]
        
        while pq:
            d, u, count = heapq.heappop(pq)
            
            if u == n - 1:
                return d
                
            if d > dist[u][count]:
                continue
                
            for v, w in adj[u]:
                if labels[v] == labels[u]:
                    new_count = count + 1
                else:
                    new_count = 1
                    
                if new_count <= k:
                    if d + w < dist[v][new_count]:
                        dist[v][new_count] = d + w
                        heapq.heappush(pq, (d + w, v, new_count))
                        
        return -1