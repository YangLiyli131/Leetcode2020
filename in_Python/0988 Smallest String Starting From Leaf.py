# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        base = 'abcdefghijklmnopqrstuvwxyz'
        d = {}
        for i in range(26):
            d[i] = base[i]
        st = []
        res = None
        if not root:
            return res
        st.append([root, d[root.val]])
        while st:
            n, v = st.pop()
            if not n.left and not n.right:
                vv = v[::-1]
                if not res:
                    res = vv
                else:
                    if res > vv:
                        res = vv
            else:
                if n.left:
                    st.append([n.left, v + d[n.left.val]])
                if n.right:
                    st.append([n.right, v + d[n.right.val]])
        return res
        