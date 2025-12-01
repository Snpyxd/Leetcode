# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node, dist):
            nonlocal ans
            if node is None:
                ans = max(ans, dist)
                return
            dfs(node.right, dist + 1)
            dfs(node.left, dist + 1)

        dfs(root, 0)
        return ans
