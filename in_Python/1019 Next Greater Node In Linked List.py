# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        res = []
        while head != None:
            res.append(head.val)
            head = head.next
        st = []
        result = []
        for i in res: result.append(0)
        for i in range(len(res)):
            while len(st) != 0 and res[st[-1]] < res[i]:
                result[st[-1]] = res[i]
                st.pop()
            st.append(i)

        return result