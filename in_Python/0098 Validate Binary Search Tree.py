# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        st = []
        res = []
        cur = root
        st.append(cur)
        while len(st) != 0:
            while cur != None:
                st.append(cur)
                cur = cur.left
            n = st.pop()
            res.append(n.val)
            cur = n.right
        for i in range(1, len(res)-1):
            if res[i] <= res[i-1]:
                return False
        return True
            