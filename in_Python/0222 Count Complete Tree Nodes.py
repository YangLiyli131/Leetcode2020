# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left = root
        right = root
        h = 0
        while right:
            left = left.left
            right = right.right
            h += 1
        if left == None:
            return pow(2,h) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        if root == None:
            return res
        q = [root]
        while q:
            n = len(q)
            while n != 0:
                n -= 1
                h = q.pop(0)
                if h.left:
                    q.append(h.left)
                if h.right:
                    q.append(h.right)
                res += 1
        return res