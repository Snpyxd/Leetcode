from collections import Counter

class Solution:
    def specialTriplets(self, nums):
        MOD = 10**9 + 7
        
        left = Counter()
        right = Counter(nums)
        
        ans = 0
        
        for j in range(len(nums)):
            val = nums[j]
            right[val] -= 1
            
            target = val * 2
            
            if left[target] and right[target]:
                ans = (ans + (left[target] * right[target]) % MOD) % MOD
            
            left[val] += 1
        
        return ans % MOD
