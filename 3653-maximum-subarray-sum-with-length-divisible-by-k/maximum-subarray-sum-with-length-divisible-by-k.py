class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        ans = float('-inf')
        min_prefix = [float('inf')] * k
        min_prefix[0] = 0

        for i, num in enumerate(nums):
            prefix += num
            r = (i + 1) % k
            ans = max(ans, prefix - min_prefix[r])
            min_prefix[r] = min(min_prefix[r], prefix)

        return ans

# Time complexity o(n)