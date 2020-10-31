# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root == None:
            return root
        q = [root]
        res = []
        while q:
            x = q.pop()
            res.append(x.val)
            if x.right:
                q.append(x.right)
            if x.left:
                q.append(x.left)
        for i in range(1, len(res)):
            root.right = TreeNode(res[i])
            root.left = None
            root = root.right
