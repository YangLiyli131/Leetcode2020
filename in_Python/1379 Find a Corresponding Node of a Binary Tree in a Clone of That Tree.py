# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        q = collections.deque()
        q.append(cloned)
        while q:
            n = len(q)
            while n != 0:
                n -= 1
                h = q.popleft()
                if h.val == target.val:
                    return h
                if h.left:
                    q.append(h.left)
                if h.right:
                    q.append(h.right)
        return None