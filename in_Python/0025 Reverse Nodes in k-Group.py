# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rev(self, head):
        pre = None
        nex = None
        cur = head
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        le = 0
        pp = head
        while pp:
            le += 1
            pp = pp.next
        revlast = 1
        if le % k != 0:
            revlast = 0
        heads = []
        cursum = 1
        h = head
        while head:
            if head.next == None and cursum < k:
                heads.append(h)
                break
            cursum += 1
            head = head.next
            if cursum == k:
                #print(h.val)
                heads.append(h)
                cursum = 1
                h = head.next
                head.next = None
                head = h
        newheads = []
        for x in heads[0: len(heads)-1]:
            newheads.append(self.rev(x))
        if revlast == 1:
            newheads.append(self.rev(heads[-1]))
        else:
            newheads.append(heads[-1])
        last = newheads[0]
        while last.next != None:
            last = last.next
        for nh in newheads[1:]:
            last.next = nh
            last = nh
            while last.next != None:
                last = last.next
        return newheads[0]