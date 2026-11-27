class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)
        min_price = min(price for _, price in items)

        div_count = [0] * n
        for i in range(n):
            fi = items[i][0]
            cnt = 0
            for j in range(n):
                if i != j and items[j][0] % fi == 0:
                    cnt += 1
            div_count[i] = cnt

        dp = [0] * (budget + 1)
        for i in range(n):
            price = items[i][1]
            weight = 1 + div_count[i]
            if price <= budget:
                for c in range(budget, price - 1, -1):
                    cand = dp[c - price] + weight
                    if cand > dp[c]:
                        dp[c] = cand

        ans = 0
        for c in range(budget + 1):
            total = dp[c] + (budget - c) // min_price
            if total > ans:
                ans = total

        return ans