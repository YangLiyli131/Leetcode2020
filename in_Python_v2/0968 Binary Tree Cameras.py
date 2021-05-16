# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        seen = {None}
        
        def dfs(node, par = None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
                if not par and node not in seen or node.left not in seen or node.right not in seen:
                    self.res += 1
                    seen.update({par, node, node.left, node.right})
            
        dfs(root)
        return self.res