# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = None
#         self.right = None
class Solution(object):
    def checkEquivalence(self, root1, root2):
        """
        :type root1: Node
        :type root2: Node
        :rtype: bool
        """
        L1 = []
        L2 = []
        st = []
        while st or root1:
            while root1:
                st.append(root1)
                root1 = root1.left
            x = st.pop()
            L1.append(x.val)
            root1 = x.right
        st = []
        while st or root2:
            while root2:
                st.append(root2)
                root2 = root2.left
            x = st.pop()
            L2.append(x.val)
            root2 = x.right
        L1.sort()
        L2.sort()
        s1 = ''.join(L1)
        s2 = ''.join(L2)
        return s1 == s2