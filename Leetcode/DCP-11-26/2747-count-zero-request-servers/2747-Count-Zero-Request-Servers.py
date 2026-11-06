from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by timestamp
        logs.sort(key=lambda l: l[1])
        
        # Sort queries while preserving their original indices
        indexed_queries = sorted(enumerate(queries), key=lambda q: q[1])
        
        ans = [0] * len(queries)
        server_count = [0] * (n + 1)
        active_servers = 0
        
        left = 0
        right = 0
        num_logs = len(logs)
        
        for orig_idx, q in indexed_queries:
            start_time = q - x
            end_time = q
            
            # Add incoming logs whose time <= end_time
            while right < num_logs and logs[right][1] <= end_time:
                s_id = logs[right][0]
                if server_count[s_id] == 0:
                    active_servers += 1
                server_count[s_id] += 1
                right += 1
                
            # Remove outdated logs whose time < start_time
            while left < num_logs and logs[left][1] < start_time:
                s_id = logs[left][0]
                server_count[s_id] -= 1
                if server_count[s_id] == 0:
                    active_servers -= 1
                left += 1
                
            # Total servers minus active servers gives servers with 0 requests
            ans[orig_idx] = n - active_servers
            
        return ans