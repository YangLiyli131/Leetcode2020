# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, nodes):
        """
        :type root: TreeNode
        :type nodes: List[TreeNode]
        """
        def solve(x):
            if not x:
                return x
            if x in nodes:
                return x
            l = solve(x.left)
            r = solve(x.right)
            if l and r:
                return x
            if l:
                return l
            if r:
                return r
        nodes = set(nodes)
        return solve(root)
        
        """
        d = {root : None}
        q = collections.deque()
        q.append(root)
        while q:
            n = len(q)
            while n != 0:
                n -= 1
                h = q.popleft()
                if h.left:
                    q.append(h.left)
                    d[h.left] = h
                if h.right:
                    q.append(h.right)
                    d[h.right] = h
        arr = set()
        base = []
        n = nodes[0]
        while n:
            arr.add(n.val)
            base.append(n.val)
            n = d[n]
        for i in range(1, len(nodes)):
            n = nodes[i]
            tmp = set()
            while n:
                tmp.add(n.val)
                n = d[n]
            arr = arr.intersection(tmp)
        for x in base:
            if x in arr:
                return TreeNode(x)
        return None
        """