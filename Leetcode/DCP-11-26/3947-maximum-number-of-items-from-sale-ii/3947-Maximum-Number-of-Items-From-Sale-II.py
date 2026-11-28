class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)
        min_price = min(price for _, price in items)
        max_factor = max(factor for factor, _ in items)

        freq = [0] * (max_factor + 1)
        for factor, _ in items:
            freq[factor] += 1

        # Count for each factor f how many other items j have factor[j] divisible by f
        div_for_factor = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if freq[f] == 0:
                continue
            cnt = freq[f] - 1
            for mult in range(2 * f, max_factor + 1, f):
                cnt += freq[mult]
            div_for_factor[f] = cnt

        cap = 2 * min_price
        candidates = []
        for factor, price in items:
            d = div_for_factor[factor]
            if d > 0 and price <= cap:
                candidates.append((price, d))

        candidates.sort(key=lambda x: x[0])

        total_items = 0
        rem_budget = budget
        for price, d in candidates:
            if rem_budget < price:
                break
            take = min(d, rem_budget // price)
            total_items += 2 * take
            rem_budget -= take * price

        total_items += rem_budget // min_price
        return total_items