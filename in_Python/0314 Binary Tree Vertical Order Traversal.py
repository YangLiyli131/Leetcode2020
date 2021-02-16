# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        r = []
        if not root:
            return r
        col = {}
        q = collections.deque()
        q.append((root,0,0))
        col[0] = [root.val]
        while q:
            h,i,j = q.popleft()
            if h.left:
                li,lj = i-1,j+1
                q.append((h.left,li,lj))
                if li not in col:
                    col[li] = [h.left.val]
                else:
                    col[li].append(h.left.val)
            if h.right:
                ri,rj = i+1,j+1
                q.append((h.right,ri,rj))
                if ri not in col:
                    col[ri] = [h.right.val]
                else:
                    col[ri].append(h.right.val)
        kk = col.keys()
        kk.sort()
        for k in kk:
            r.append(col[k])
        return r