# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        st = []
        if t == None:
            return ""
        st.append(t)
        res = ""
        while st:
            h = st.pop()
            if h == ')':
                res += h
                continue
            res += '(' + str(h.val)
            if h.left == None and h.right != None:
                res += "()"
            if h.right:
                st.append(')')
                st.append(h.right)
            if h.left:
                st.append(')')
                st.append(h.left)
        return res[1:]