# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None
        d = {}
        all_depth = []
        def dfs(node):
            if not node:
                return 0
            dep = max(dfs(node.left), dfs(node.right)) + 1
            if node.val not in d:
                d[node.val] = [dep]
            else:
                d[node.val].append(dep)
            all_depth.append(dep)
            return dep
        dfs(root)
        md = max(all_depth)
        res = []
        for i in range(md):
            res.append([])
        for k in d:
            for v in d[k]:
                res[v-1].append(k)
        return res