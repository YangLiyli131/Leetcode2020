# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        A = {}
        q = collections.deque()
        q.append(root)
        while q:
            n = len(q)
            while n != 0:
                n -= 1
                h = q.popleft()
                if h.left:
                    if h.val not in A:
                        A[h.val] = [h.left.val]
                    else:
                        A[h.val].append(h.left.val)
                    if h.left.val not in A:
                        A[h.left.val] = [h.val]
                    else:
                        A[h.left.val].append(h.val)
                    q.append(h.left)
                if h.right:
                    if h.val not in A:
                        A[h.val] = [h.right.val]
                    else:
                        A[h.val].append(h.right.val)
                    if h.right.val not in A:
                        A[h.right.val] = [h.val]
                    else:
                        A[h.right.val].append(h.val)
                    q.append(h.right)
        q = collections.deque()
        q.append(target.val)
        seen = set()
        res = []
        level = -1
        seen.add(target.val)
        while q:
            n = len(q)
            cur = []
            level += 1
            while n != 0:
                n -= 1
                h = q.popleft()
                if h in A:
                    for nex in A[h]:
                        if nex not in seen:
                            seen.add(nex)
                            q.append(nex)
                cur.append(h)
            if level == K:
                res = cur[:]
                break
        return res
        