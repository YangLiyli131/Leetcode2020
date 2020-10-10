# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if root == None:
            return res
        st = []
        st.append([root, 0, []])
        while st:
            prev, value, path  = st.pop()
            pathh = path[:]
            if prev.left == None and prev.right == None:
                if value + prev.val == sum:
                    path.append(prev.val)
                    res.append(path)
            if prev.right != None:
                path.append(prev.val)
                st.append([prev.right, value + prev.val, path])
            if prev.left != None:
                pathh.append(prev.val)
                st.append([prev.left, value + prev.val, pathh])
        return res