class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        pos = []
        neg = []
        contain_zero = False
        for a in A:
            if a == 0:
                contain_zero = True
            elif a < 0:
                neg.append(a)
            else:
                pos.append(a)
        neg.sort()
        while K != 0 and len(neg) != 0:
            K -= 1
            pos.append(-neg.pop(0))
        if len(neg) != 0:
            for x in neg:
                pos.append(x)
            return sum(pos)
        if K != 0:
            if contain_zero or K % 2 == 0:
                return sum(pos)
            else:
                pos.sort()
                pos[0] = -pos[0]
        return sum(pos)
        
        