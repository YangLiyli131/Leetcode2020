# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if t == None:
            return True
        
        def isI(a, b):
            if a == None and b == None:
                return True
            if a == None or b == None:
                return False
            if a.val != b.val:
                return False
            return isI(a.left, b.left) and isI(a.right, b.right)
    
        q = []
        if s == None and t == None:
            return True
        if s == None or t == None:
            return False
        q.append(s)
        while q:
            n = len(q)
            while n != 0:
                n -= 1
                h = q.pop()
                if isI(h,t):
                    return True
                if h.left:
                    q.append(h.left)
                if h.right:
                    q.append(h.right)
        return False