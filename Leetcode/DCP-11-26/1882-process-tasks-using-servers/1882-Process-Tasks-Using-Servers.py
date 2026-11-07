from typing import List
import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        n = len(servers)
        m = len(tasks)
        
        # Min-heap for free servers: stores (weight, index)
        free_servers = []
        for i, weight in enumerate(servers):
            heapq.heappush(free_servers, (weight, i))
            
        # Min-heap for busy servers: stores (free_time, weight, index)
        busy_servers = []
        
        ans = [0] * m
        current_time = 0
        
        for j in range(m):
            # Fast-forward time if no servers are free and current_time is before task arrival
            current_time = max(current_time, j)
            
            # If there are no free servers available, jump time to the earliest server release time
            if not free_servers and busy_servers[0][0] > current_time:
                current_time = busy_servers[0][0]
                
            # Release all servers that become free at or before current_time
            while busy_servers and busy_servers[0][0] <= current_time:
                free_time, weight, index = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, index))
                
            # Assign the task to the best available server
            weight, index = heapq.heappop(free_servers)
            ans[j] = index
            
            # Push the server into the busy heap with its new release time
            release_time = current_time + tasks[j]
            heapq.heappush(busy_servers, (release_time, weight, index))
            
        return ans