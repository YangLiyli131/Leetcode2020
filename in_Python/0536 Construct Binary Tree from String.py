# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """       
        def h(s):
            if not s:
                return None
            i = 0
            while i < len(s) and s[i] not in ['(',')']:
                i += 1
            start = s[:i]
            ro = TreeNode(int(start))
            nexts = s[i:]
            summ = 0
            idx = -1
            for i in range(len(nexts)):
                if nexts[i] == '(':
                    summ -= 1
                if nexts[i] == ')':
                    summ += 1
                if summ == 0:
                    idx = i
                    break
            l,r = nexts[1:idx], nexts[idx+2:-1]
            ro.left = h(l)
            ro.right = h(r)
            return ro
        return h(s)