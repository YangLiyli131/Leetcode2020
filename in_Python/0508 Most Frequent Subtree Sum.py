# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        d = {}
        if not root:
            return []
        def helper(n):
            if not n:
                return 0
            l = helper(n.left)
            r = helper(n.right)
            c = n.val + l + r
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
            return c
        helper(root)
        cc = {}
        for k in d:
            v = d[k]
            if v not in cc:
                cc[v] = [k]
            else:
                cc[v].append(k)
        return cc[max(cc.keys())]
        
        