from collections import Counter
from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        factor_counts = [0] * (n + 1)
        for factor, _ in items:
            factor_counts[factor] += 1

        # mult_count[f] = total items whose factor is a multiple of f
        mult_count = [0] * (n + 1)
        for f in range(1, n + 1):
            total = 0
            for m in range(f, n + 1, f):
                total += factor_counts[m]
            mult_count[f] = total

        # Group identical (factor, price) pairs to keep option count O(n)
        group_counts = Counter((factor, price) for factor, price in items)

        # Each entry: (scaled_cost_per_item, bundle_cost, items_gained, max_batches)
        # max_batches = -1 represents unlimited copies
        options = []
        for (factor, price), cnt in group_counts.items():
            out_deg = max(0, mult_count[factor] - 1)
            freebie_batches = cnt * out_deg
            if freebie_batches > 0:
                options.append((price, price, 2, freebie_batches))
            options.append((price * 2, price, 1, -1))

        # Prefer lower scaled cost per item, then larger item gain per bundle
        options.sort(key=lambda x: (x[0], -x[2], x[1]))

        total_items = 0
        rem_budget = budget

        for _, bundle_cost, gain, max_batches in options:
            if rem_budget < bundle_cost:
                continue
            affordable = rem_budget // bundle_cost
            take = affordable if max_batches == -1 else min(affordable, max_batches)
            total_items += take * gain
            rem_budget -= take * bundle_cost

        return total_items