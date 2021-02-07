# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            V = TreeNode(v)
            V.left = root
            return V
        q = collections.deque()
        q.append(root)
        while q:
            d -= 1
            n = len(q)
            while n != 0:
                n -= 1
                h = q.popleft()
                if d == 1:
                    t1 = h.left
                    t2 = h.right
                    h.left = TreeNode(v)
                    h.right = TreeNode(v)
                    h.left.left = t1
                    h.right.right = t2
                else:
                    if h.left:
                        q.append(h.left)
                    if h.right:
                        q.append(h.right)
        return root
                
            