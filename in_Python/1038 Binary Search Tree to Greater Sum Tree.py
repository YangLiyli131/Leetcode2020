# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        trav = []
        st = []
        r = root
        while r or st:
            while r != None:
                st.append(r)
                r = r.left
            rx = st.pop()
            trav.append(rx.val)
            r = rx.right
        d = {}
        for i in range(len(trav)-2, -1, -1):
            k = trav[i]
            trav[i] = trav[i+1] + k
            d[k] = trav[i]
        d[trav[-1]] = trav[-1]
        st = []
        r = root
        while r or st:
            while r != None:
                st.append(r)
                r = r.left
            rx = st.pop()
            rx.val = d[rx.val]
            r = rx.right
        return root
        