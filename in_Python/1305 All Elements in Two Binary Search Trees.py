# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tra(self, root):
        res = []
        st = []
        n = root
        while n != None or len(st) != 0:
            while n != None:
                st.append(n)
                n = n.left
            n = st.pop()
            res.append(n.val)
            n = n.right
        return res
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        res1 = self.tra(root1)
        res2 = self.tra(root2)
        res = []
        id1 = 0
        id2 = 0
        while id1 < len(res1) and id2 < len(res2):
            if res1[id1] < res2[id2]:
                res.append(res1[id1])
                id1 += 1
            elif res1[id1] > res2[id2]:
                res.append(res2[id2])
                id2 += 1
            else:
                res.append(res2[id2])
                res.append(res2[id2])
                id1 += 1
                id2 += 1
        while id1 < len(res1):
            res.append(res1[id1])
            id1 += 1
        while id2 < len(res2):
            res.append(res2[id2])
            id2 += 1         
        return res