class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Strategy 1: Buy only individual type 1 and type 2 items
        cost_a = need1 * cost1 + need2 * cost2
        
        # Strategy 2: Buy only type 3 bundles to cover the maximum need
        cost_b = costBoth * max(need1, need2)
        
        # Strategy 3: Buy type 3 bundles for the overlapping needs, and individual items for the remainder
        mn = min(need1, need2)
        cost_c = costBoth * mn + (need1 - mn) * cost1 + (need2 - mn) * cost2
        
        return min(cost_a, cost_b, cost_c)