# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 == root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        
        lf1 = []
        st = []
        n = root1
        while n or st:
            while n:
                st.append(n)
                n = n.left
            n = st.pop()
            if n.right == None and n.left == None:
                lf1.append(n.val)
            n = n.right
        lf2 = []
        st = []
        n = root2
        while n or st:
            while n:
                st.append(n)
                n = n.left
            n = st.pop()
            if n.right == None and n.left == None:
                lf2.append(n.val)
            n = n.right
        #print(lf1)
        #print(lf2)
        if len(lf1) != len(lf2):
            return False
        for i in range(len(lf1)):
            if lf1[i] != lf2[i]:
                return False
        return True