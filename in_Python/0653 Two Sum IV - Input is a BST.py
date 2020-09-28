# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root == None:
            return False
        q = []
        q.append(root)
        values = []
        values.append(root.val)
        while len(q) != 0:
            n = len(q)
            for i in range(n):
                h = q.pop(0)
                if h.left != None:
                    if k - h.left.val in values:
                        return True
                    else:
                        q.append(h.left)
                        values.append(h.left.val)
                if h.right != None:
                    if k - h.right.val in values:
                        return True
                    else:
                        q.append(h.right)
                        values.append(h.right.val)
                values.append(h.val)
        return False