# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        
        def dfs(node):
            if not node:
                return True
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right and (not node.left or node.left.val == node.val) and (not node.right or node.val == node.right.val):
                self.res += 1
                return True
            return False
        
        dfs(root)
        return self.res
            
            
        