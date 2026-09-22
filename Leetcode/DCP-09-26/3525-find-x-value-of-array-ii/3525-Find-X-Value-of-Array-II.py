class SegmentTreeNode:
    def __init__(self, k: int):
        self.k = k
        self.prod = 1
        self.remain = [0] * k

class SegmentTree:
    def __init__(self, nums: list[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree = [SegmentTreeNode(k) for _ in range(4 * self.n)]
        self.build(nums, 0, 0, self.n - 1)

    def merge(self, left: SegmentTreeNode, right: SegmentTreeNode) -> SegmentTreeNode:
        res = SegmentTreeNode(self.k)
        res.prod = (left.prod * right.prod) % self.k
        
        for r in range(self.k):
            res.remain[r] = left.remain[r]
            
        for r in range(self.k):
            new_r = (r * left.prod) % self.k
            res.remain[new_r] += right.remain[r]
            
        return res

    def build(self, nums: list[int], node: int, l: int, r: int):
        if l == r:
            val = nums[l] % self.k
            self.tree[node].prod = val
            self.tree[node].remain[val] = 1
            return
        
        mid = (l + r) // 2
        self.build(nums, 2 * node + 1, l, mid)
        self.build(nums, 2 * node + 2, mid + 1, r)
        self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def update(self, node: int, l: int, r: int, idx: int, val: int):
        if l == r:
            val %= self.k
            self.tree[node].remain = [0] * self.k
            self.tree[node].prod = val
            self.tree[node].remain[val] = 1
            return
            
        mid = (l + r) // 2
        if idx <= mid:
            self.update(2 * node + 1, l, mid, idx, val)
        else:
            self.update(2 * node + 2, mid + 1, r, idx, val)
            
        self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, node: int, l: int, r: int, ql: int, qr: int) -> SegmentTreeNode:
        if ql <= l and r <= qr:
            return self.tree[node]
            
        mid = (l + r) // 2
        if qr <= mid:
            return self.query(2 * node + 1, l, mid, ql, qr)
        if ql > mid:
            return self.query(2 * node + 2, mid + 1, r, ql, qr)
            
        left_res = self.query(2 * node + 1, l, mid, ql, qr)
        right_res = self.query(2 * node + 2, mid + 1, r, ql, qr)
        return self.merge(left_res, right_res)


class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)
        tree = SegmentTree(nums, k)
        ans = []
        
        for idx, val, start, x in queries:
            tree.update(0, 0, n - 1, idx, val)
            node_res = tree.query(0, 0, n - 1, start, n - 1)
            ans.append(node_res.remain[x])
            
        return ans