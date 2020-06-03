# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rev(self, n):
        pre = None
        cur = n
        nextn = None
        while cur != None:
            nextn = cur.next
            cur.next = pre
            pre = cur
            cur = nextn
        return pre
            
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        L = 0
        h = head
        while h != None:
            h = h.next
            L += 1
        mid = L/2
        newH = head
        while mid != 0:
            newH = newH.next
            mid -= 1
        if L % 2 == 1:
            newH = newH.next
        mid = L/2
        
        nh = self.rev(newH)
        while mid != 0:
            if head.val != nh.val:
                return False
            head = head.next
            nh = nh.next
            mid -= 1
        return True
    