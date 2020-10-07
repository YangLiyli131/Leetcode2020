# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = []
        idx = 0
        q.append(root)
        while len(q) != 0:
            n = len(q)
            level = []
            for i in range(n):
                h = q.pop(0)
                if h.left != None:
                    q.append(h.left)
                if h.right != None:
                    q.append(h.right)
                level.append(h.val)
            if idx % 2 == 0:
                if level[-1] % 2 == 0:
                    return False
                for i in range(len(level)-1):
                    if level[i] % 2 == 0:
                        return False
                    if level[i] >= level[i+1]:
                        return False
            else:
                if level[-1] % 2 == 1:
                    return False
                for i in range(len(level)-1):
                    if level[i] % 2 == 1:
                        return False
                    if level[i] <= level[i+1]:
                        return False
            idx += 1
        return True