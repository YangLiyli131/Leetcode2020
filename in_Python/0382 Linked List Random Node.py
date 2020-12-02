# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.h = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        n = 0
        nd = self.h
        while nd:
            n += 1
            nd = nd.next 
        nd = self.h
        for i in range(random.randrange(n)):
            nd = nd.next
        return nd.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()