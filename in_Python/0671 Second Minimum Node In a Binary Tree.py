# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float('Inf')
        low = root.val
        
        def dfs(node):
            if node:
                if low < node.val < self.res:
                    self.res = node.val
                elif node.val == low:
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        return self.res if self.res < float('Inf') else -1
            