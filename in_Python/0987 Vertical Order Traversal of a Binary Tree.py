# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d = {}
        res = []
        q = [[root,0,0]]
        while q:
            n = len(q)
            while n != 0:
                n -= 1
                [h,x,y] = q.pop(0)
                if x not in d:
                    d[x] = [[h.val,y]]
                else:
                    d[x].append([h.val,y])
                if h.left:
                    q.append([h.left, x-1, y-1])
                if h.right:
                    q.append([h.right, x+1, y-1])
        ky = d.keys()
        ky.sort()
        for k in ky:
            cur = d[k]
            cur = sorted(cur, key = lambda x : (-x[1],x[0]))
            tmp = []
            for x in cur:
                tmp.append(x[0])
            res.append(tmp)
        return res