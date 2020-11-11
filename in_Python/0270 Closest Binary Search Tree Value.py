# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.cur_dif = sys.maxint
        self.res = None
        
        def search(r, t):
            if r == None:
                return
            if r.val > t:
                d = abs(r.val - t)
                if d < self.cur_dif:
                    self.cur_dif = d
                    self.res = r.val
                search(r.left, t)
            else:
                d = abs(r.val - t)
                if d < self.cur_dif:
                    self.cur_dif = d
                    self.res = r.val
                search(r.right, t)
        search(root, target)
        return self.res
            