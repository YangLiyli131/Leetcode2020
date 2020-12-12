# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 1
        q = collections.deque()
        q.append([root, root.val])
        while q:
            n = len(q)
            while n != 0:
                n -= 1
                h,v = q.popleft()
                if h.left:
                    if h.left.val >= v:
                        res += 1
                    q.append([h.left, max(v, h.left.val)])
                if h.right:
                    if h.right.val >= v:
                        res += 1
                    q.append([h.right, max(v, h.right.val)])
        return res