# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def check(self, L):
        i = 0
        j = len(L)-1
        while i < j:
            if L[i] != L[j]:
                return False
            i += 1
            j -= 1
        return True
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = []
        q.append(root)
        res = []
        while len(q) != 0:
            n = len(q)
            cur = []
            for i in range(n):
                h = q.pop(0)
                if h == None:
                    cur.append(None)
                    continue
                if h.left != None:
                    q.append(h.left)
                else:
                    q.append(None)
                if h.right != None:
                    q.append(h.right)
                else:
                    q.append(None)
                if h != None:
                    cur.append(h.val)
            res.append(cur)
        #print(res)
        for r in res:
            if not self.check(r):
                return False
        return True
            
            