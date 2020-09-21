# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        st = []
        if root == None:
            return None
        st.append(root)
        while len(st) != 0:
            cn = st.pop()
            res.append(cn.val)
            if cn.left != None:
                st.append(cn.left)
            if cn.right != None:
                st.append(cn.right)
        dict = {}
        for i in res:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] = dict[i] + 1
        maxnum = []
        curmax = 0
        for k in dict:
            if dict[k] > curmax:
                curmax = dict[k]
                maxnum = []
                maxnum.append(k)
            elif dict[k] == curmax:
                maxnum.append(k)
        return maxnum