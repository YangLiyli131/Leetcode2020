# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findNearestRightNode(self, root, u):
        """
        :type root: TreeNode
        :type u: TreeNode
        :rtype: TreeNode
        """
        if root == None or u == None:
            return None
        q = [root]
        while q:
            n = len(q)
            cur = []
            idx = 0
            loc = -1
            while n != 0:
                n -= 1
                h = q.pop(0)
                if h.val == u.val:
                    loc = idx
                idx += 1
                cur.append(h)
                if h.left:
                    q.append(h.left)
                if h.right:
                    q.append(h.right)
            if loc == -1:
                continue
            if loc == len(cur)-1:
                return None
            return cur[loc+1]
        return None