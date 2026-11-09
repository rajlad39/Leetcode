from typing import List
import heapq
import bisect

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # Min-heap to track busy servers: stores tuples of (finish_time, server_id)
        busy = []
        
        # A list representing currently available servers (kept sorted)
        # Initially all servers from 0 to k-1 are available
        available = list(range(k))
        
        request_counts = [0] * k
        
        for i in range(len(arrival)):
            curr_time = arrival[i]
            dur = load[i]
            
            # 1. Free up servers that have finished their tasks by curr_time
            while busy and busy[0][0] <= curr_time:
                _, s_id = heapq.heappop(busy)
                # Insert back into sorted available list
                idx = bisect.bisect_left(available, s_id)
                available.insert(idx, s_id)
                
            # If no servers are available, drop the request
            if not available:
                continue
                
            # 2. Find the preferred server using (i % k)
            target = i % k
            idx = bisect.bisect_left(available, target)
            
            # If no server >= target is available, wrap around to the beginning (index 0)
            if idx == len(available):
                idx = 0
                
            server_id = available.pop(idx)
            
            # 3. Assign the request to this server
            request_counts[server_id] += 1
            finish_time = curr_time + dur
            heapq.heappush(busy, (finish_time, server_id))
            
        # 4. Find all busiest servers
        max_requests = max(request_counts)
        return [i for i, count in enumerate(request_counts) if count == max_requests]