class Solution:
    def fib(self, n: int) -> int:
        dp = [-1] * (n + 1)

        def solve(x):
            if x <= 1:
                return x

            if dp[x] != -1:
                return dp[x]

            dp[x] = solve(x - 1) + solve(x - 2)
            return dp[x]

        return solve(n)
