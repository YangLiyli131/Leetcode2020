# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = []
        q.append(root)
        n = []
        while len(q) != 0:
            x = len(q)
            for i in range(x):
                h = q.pop(0)
                if h.left != None:
                    if len(n) != 0 and h.left.val != n[-1] or h.left.val != h.val:
                        return False
                    q.append(h.left)
                if h.right != None:
                    if len(n) != 0 and h.right.val != n[-1] or h.right.val != h.val:
                        return False
                    q.append(h.right)
                n.append(h.val)
        return True
        