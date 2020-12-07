"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        d = {head : Node(head.val)}
        q = collections.deque([head])
        while q:
            h = q.popleft()
            if h.next:
                if h.next not in d:
                    d[h.next] = Node(h.next.val)
                    q.append(h.next)
                d[h].next = d[h.next]
            if h.random:
                if h.random not in d:
                    d[h.random] = Node(h.random.val)
                    q.append(h.random)
                d[h].random = d[h.random]
        return d[head]