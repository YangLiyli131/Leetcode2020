# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        q = []
        res = []
        if root == None:
            return res
        q.append(root)
        while len(q) != 0:
            n = len(q)
            cur = []
            for i in range(n):
                h = q.pop(0)
                if h.left != None:
                    q.append(h.left)
                if h.right != None:
                    q.append(h.right)
                cur.append(h.val)
            res.append(cur[-1])
        return res
        