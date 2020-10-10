# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        st = []
        cur = root
        while cur != None or len(st) != 0:
            while cur != None:
                st.append(cur)
                cur = cur.left
            cur = st.pop()
            res.append(cur.val)
            cur = cur.right
        x = res[1] - res[0]
        for i in range(2, len(res)):
            x = min(x, res[i] - res[i-1])
        return x