# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = []
        h = head
        while h:
            arr.append(h.val)
            h = h.next
        
        op = True
        while op:
            op = False
            cs = [0]
            for x in arr:
                cs.append(cs[-1] + x)
            d = {}
            for i in range(len(cs)):
                cur = cs[i]
                if cur in d:
                    d[cur].append(i)
                else:
                    d[cur] = [i]
            
            for key in d:
                if len(d[key]) >= 2:
                    op = True
                    left = d[key][0]
                    right = d[key][1]
                    tmp = []
                    for j in range(len(arr)):
                        if j not in list(range(left,right)):
                            tmp.append(arr[j])
                    arr = tmp
                    break
        if len(arr) == 0:
            return None
        nh = ListNode(0)
        h = ListNode(arr[0])
        nh.next = h
        for x in arr[1:]:
            h.next = ListNode(x)
            h = h.next
        return nh.next
                    
        