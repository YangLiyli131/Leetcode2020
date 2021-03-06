# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return [-1,-1,-1]
            left,right = dfs(root.left), dfs(root.right)
            return [left[1]+1, right[0]+1, max(left[2], right[2], left[1]+1, right[0]+1)]
        return dfs(root)[-1]