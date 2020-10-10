# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        num = []
        st = []
        st.append([root, []])
        while st:
            n, path = st.pop()
            pathh = path[:]
            if n.left == None and n.right == None:
                path.append(n.val)
                num.append(path)
            if n.right != None:
                path.append(n.val)
                st.append([n.right, path])
            if n.left != None:
                pathh.append(n.val)
                st.append([n.left, pathh])
        res = 0
        for x in num:
            cur = 0
            p = 0
            while x:
                last = x.pop()
                cur += last * pow(2, p)
                p += 1
            res += cur
        return res