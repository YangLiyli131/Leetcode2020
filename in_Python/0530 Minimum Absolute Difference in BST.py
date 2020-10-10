# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        st = []
        n = root
        while n or st:
            while n:
                st.append(n)
                n = n.left
            n = st.pop()
            res.append(n.val)
            n = n.right
        x = res[1] - res[0]
        for i in range(2, len(res)):
            x = min(x, res[i] - res[i-1])
        return x