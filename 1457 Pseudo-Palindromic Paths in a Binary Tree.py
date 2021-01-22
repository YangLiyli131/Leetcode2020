# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = collections.deque()
        tm = [0] * 9
        tm[root.val-1] = 1
        q.append([root, tm])
        res = 0
        while q:
            n = len(q)
            while n != 0:
                n -= 1
                h = q.popleft()
                r = h[0]
                l = h[1]
                if r.left:
                    ll = l[:]
                    ll[r.left.val-1] += 1
                    q.append([r.left, ll])
                if r.right:
                    lll = l[:]
                    lll[r.right.val-1] += 1
                    q.append([r.right, lll])
                if not r.left and not r.right:
                    odd = 0
                    for x in l:
                        if x % 2 == 1:
                            odd += 1
                    if odd <= 1:
                        res += 1
        return res
        
        
        