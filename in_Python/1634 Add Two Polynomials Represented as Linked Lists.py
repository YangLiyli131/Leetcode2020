# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1, poly2):
        """
        :type poly1: PolyNode
        :type poly2: PolyNode
        :rtype: PolyNode
        """
        pre = PolyNode(0,0)
        head = pre
        h1 = poly1
        h2 = poly2
        while h1 and h2:
            if h1.power > h2.power:
                pre.next = h1
                h1 = h1.next
                pre = pre.next
            elif h1.power < h2.power:
                pre.next = h2
                h2 = h2.next
                pre = pre.next
            else:
                newco = h1.coefficient + h2.coefficient
                if newco != 0:
                    newnode = PolyNode(newco, h1.power)
                    pre.next = newnode
                    pre = pre.next
                h1 = h1.next
                h2 = h2.next          
        pre.next = None
        if h1:
            pre.next = h1
        if h2:
            pre.next = h2
        return head.next
        