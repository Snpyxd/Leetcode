# class Solution:
#     def climbStairs(self, n: int) -> int:
        # bottom up
        # if n <= 1:
        #     return 1

        # prev = 1
        # curr = 1

        # for i in range(2, n+1):
        #     next = prev + curr
        #     prev = curr
        #     curr = next

        # return curr
        # top down
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

       
        dp = [0] * (n + 2)   
        dp[n] = 1
        dp[n - 1] = 1

        for i in range(n - 2, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]

        return dp[0]
