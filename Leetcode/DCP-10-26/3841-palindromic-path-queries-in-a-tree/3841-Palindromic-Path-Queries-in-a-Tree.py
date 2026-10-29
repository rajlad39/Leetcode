import sys
from typing import List

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

class SegmentTree:
    def __init__(self, size: int):
        self.n = size
        self.tree = [0] * (4 * size)

    def update(self, node: int, start: int, end: int, idx: int, mask: int):
        if start == end:
            self.tree[node] = mask
            return
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node, start, mid, idx, mask)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, mask)
        self.tree[node] = self.tree[2 * node] ^ self.tree[2 * node + 1]

    def query(self, node: int, start: int, end: int, l: int, r: int) -> int:
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left_val = self.query(2 * node, start, mid, l, r)
        right_val = self.query(2 * node + 1, mid + 1, end, l, r)
        return left_val ^ right_val


class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [0] * n
        depth = [0] * n
        heavy = [-1] * n
        size = [0] * n

        # DFS 1: Calculate sizes, depths, parents, and heavy edges
        def dfs(u, p, d):
            parent[u] = p
            depth[u] = d
            size[u] = 1
            max_size = 0
            for v in adj[u]:
                if v != p:
                    dfs(v, u, d + 1)
                    size[u] += size[v]
                    if size[v] > max_size:
                        max_size = size[v]
                        heavy[u] = v

        dfs(0, -1, 0)

        head = [0] * n
        pos = [0] * n
        cur_pos = 0

        # DFS 2: Decompose tree into heavy chains
        def decompose(u, h):
            nonlocal cur_pos
            head[u] = h
            pos[u] = cur_pos
            cur_pos += 1

            if heavy[u] != -1:
                decompose(heavy[u], h)

            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    decompose(v, v)

        decompose(0, 0)

        seg_tree = SegmentTree(n)
        s_chars = list(s)

        # Initialize Segment Tree
        for i in range(n):
            bit = 1 << (ord(s_chars[i]) - ord('a'))
            seg_tree.update(1, 0, n - 1, pos[i], bit)

        # Helper: Query path between u and v using HLD
        def query_path(u: int, v: int) -> int:
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                res ^= seg_tree.query(1, 0, n - 1, pos[head[u]], pos[u])
                u = parent[head[u]]
            if depth[u] > depth[v]:
                u, v = v, u
            res ^= seg_tree.query(1, 0, n - 1, pos[u], pos[v])
            return res

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                s_chars[u] = c
                bit = 1 << (ord(c) - ord('a'))
                seg_tree.update(1, 0, n - 1, pos[u], bit)
            else:
                u = int(parts[1])
                v = int(parts[2])
                mask = query_path(u, v)
                # Palindrome check: at most 1 bit set in mask
                is_palindrome = (mask & (mask - 1)) == 0
                ans.append(is_palindrome)

        return ans