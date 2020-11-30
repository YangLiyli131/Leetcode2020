"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        d = {node : Node(node.val)}
        q = collections.deque([node])
        while q:
            r = q.popleft()
            for nex in r.neighbors:
                if nex not in d:
                    d[nex] = Node(nex.val)
                    q.append(nex)
                d[r].neighbors.append(d[nex])
        return d[node]