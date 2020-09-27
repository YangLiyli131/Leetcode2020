class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sa = 0
        sb = 0
        res = []
        for a in A:
            sa += a
        for b in B:
            sb += b
        for a in A:
            if a - (sa - sb) / 2 in B:
                res.append(a)
                res.append(a - (sa - sb) / 2)
                break
        return res