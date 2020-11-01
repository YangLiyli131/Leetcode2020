# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        q = [root]
        p1 = None
        p2 = None
        l1 = -1
        l2 = -1
        l = 0
        while q:
            n = len(q)
            l += 1
            while n != 0:
                n -= 1
                h = q.pop(0)
                if h.left:
                    if h.left.val == x:
                        p1 = h
                        l1 = l
                    if h.left.val == y:
                        p2 = h
                        l2 = l
                    q.append(h.left)
                if h.right:
                    if h.right.val == x:
                        p1 = h
                        l1 = l
                    if h.right.val == y:
                        p2 = h
                        l2 = l
                    q.append(h.right)
                if p1 and p2:
                    return p1 != p2 and l1 == l2
        return False