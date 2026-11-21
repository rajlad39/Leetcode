class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)

        final_tree = [[] for _ in range(n)]
        last_seen = [-1] * 26

        # Iterative DFS to determine each node's final parent without recursion limit issues
        # State: (node, stage) where stage 0 = enter, stage 1 = exit/restore
        stack = [(0, 0)]
        prev_stack = []

        while stack:
            u, stage = stack.pop()
            idx = ord(s[u]) - ord('a')
            if stage == 0:
                if u > 0:
                    new_parent = last_seen[idx] if last_seen[idx] != -1 else parent[u]
                    final_tree[new_parent].append(u)
                prev_stack.append((u, last_seen[idx]))
                last_seen[idx] = u
                stack.append((u, 1))
                for v in reversed(adj[u]):
                    stack.append((v, 0))
            else:
                node_u, prev_val = prev_stack.pop()
                last_seen[ord(s[node_u]) - ord('a')] = prev_val

        # Iterative post-order traversal on final_tree for subtree sizes
        ans = [1] * n
        order = []
        dfs_stack = [0]
        while dfs_stack:
            u = dfs_stack.pop()
            order.append(u)
            for v in final_tree[u]:
                dfs_stack.append(v)

        for u in reversed(order):
            total = 1
            for v in final_tree[u]:
                total += ans[v]
            ans[u] = total

        return ans