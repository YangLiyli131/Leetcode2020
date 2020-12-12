# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """    
        res = []
        def dfs(node):
            if not node:
                return 0
            tmp = node.val + dfs(node.left) + dfs(node.right) - 1
            res.append(tmp)
            return tmp
        
        dfs(root)
        r = 0
        for x in res:
            r += abs(x)
        return r