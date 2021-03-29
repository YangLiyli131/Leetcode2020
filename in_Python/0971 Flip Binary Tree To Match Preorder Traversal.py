# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        self.res = []
        self.i = 0
        def dfs(n):
            if n:
                if n.val != voyage[self.i]:
                    self.res = [-1]
                    return 
                self.i += 1
                if self.i < len(voyage) and n.left and n.left.val != voyage[self.i]:
                    self.res.append(n.val)
                    dfs(n.right)
                    dfs(n.left)
                else:
                    dfs(n.left)
                    dfs(n.right)
        dfs(root)
        if self.res and self.res[0] == -1:
            self.res = [-1]
        return self.res