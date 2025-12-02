class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        from collections import defaultdict

        MOD = 10**9 + 7   # the problem requires modulo

        # 1. Count how many points exist at each y-level
        ycount = defaultdict(int)
        for x, y in points:
            ycount[y] += 1

        # 2. For each y-level compute C(k, 2)
        segments = []
        for k in ycount.values():
            if k >= 2:
                segments.append(k * (k - 1) // 2)

        # 3. Count trapezoids by combining segments from different y-levels
        ans = 0
        prefix_sum = 0

        for seg in segments:
            ans = (ans + seg * prefix_sum) % MOD
            prefix_sum = (prefix_sum + seg) % MOD

        return ans
