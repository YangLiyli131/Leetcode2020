# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.val = 0
        def dfs(root):
            if root:
                dfs(root.right)
                root.val += self.val
                self.val = root.val
                dfs(root.left)
        dfs(root)
        return root