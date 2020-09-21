class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        evens = []
        odds = []
        for a in A:
            if a % 2 == 0:
                evens.append(a)
            else:
                odds.append(a)
        res = []
        eid = 0
        oid = 0
        for i in range(len(A)):
            if i % 2 == 0:
                res.append(evens[eid])
                eid += 1
            else:
                res.append(odds[oid])
                oid += 1
        return res