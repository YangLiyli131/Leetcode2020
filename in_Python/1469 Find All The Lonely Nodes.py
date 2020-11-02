# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        q = [root]
        while q:
            n = len(q)
            while n != 0:
                n -= 1
                h = q.pop(0)
                if h.left and h.right:
                    q.append(h.left)
                    q.append(h.right)
                elif h.left:
                    q.append(h.left)
                    arr.append(h.left.val)
                elif h.right:
                    q.append(h.right)
                    arr.append(h.right.val)
        return arr