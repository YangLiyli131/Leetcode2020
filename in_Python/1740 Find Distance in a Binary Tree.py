# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDistance(self, root, p, q):
        """
        :type root: TreeNode
        :type p: int
        :type q: int
        :rtype: int
        """
        al = {}
        qq = collections.deque()
        qq.append(root)
        while qq:
            n = len(qq)
            while n != 0:
                n -= 1
                h = qq.popleft()
                if h.left:
                    qq.append(h.left)
                    if h.val not in al:
                        al[h.val] = [h.left.val]
                    else:
                        al[h.val].append(h.left.val)
                    if h.left.val not in al:
                        al[h.left.val] = [h.val]
                    else:
                        al[h.left.val].append(h.val)
                if h.right:
                    qq.append(h.right)
                    if h.val not in al:
                        al[h.val] = [h.right.val]
                    else:
                        al[h.val].append(h.right.val)
                    if h.right.val not in al:
                        al[h.right.val] = [h.val]
                    else:
                        al[h.right.val].append(h.val)
        res = -1
        v = set()
        v.add(p)
        qq = collections.deque()
        qq.append(p)
        while qq:
            n = len(qq)
            res += 1
            while n != 0:
                n -= 1
                h = qq.popleft()
                if h == q:
                    return res
                if h in al:
                    for nex in al[h]:
                        if nex not in v:
                            v.add(nex)
                            qq.append(nex)
        return -1
        