class Solution:
    def minMirrorPairDistance(self, nums):
        ans = float('inf')
        n = len(nums)
        mp = {}
        
        for i in range(n - 1, -1, -1):
            s = str(nums[i])
            k = s[::-1]
            trimmed = s.rstrip('0')
            
            if trimmed in mp:
                ans = min(ans, mp[trimmed] - i)
            
            mp[k] = i
        
        return -1 if ans == float('inf') else ans
