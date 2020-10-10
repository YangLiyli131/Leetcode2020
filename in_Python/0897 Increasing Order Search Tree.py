# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
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
        T = TreeNode(res[0])
        Tx = T
        for i in range(1, len(res)):
            cur = TreeNode(res[i])
            Tx.right = cur
            Tx = Tx.right
        return T