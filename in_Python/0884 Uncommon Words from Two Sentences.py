class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        res = []
        d1 = {}
        d2 = {}
        a = A.split(' ')
        b = B.split(' ')
        for sa in a:
            if sa not in d1:
                d1[sa] = 1
            else:
                d1[sa] += 1
        for sb in b:
            if sb not in d2:
                d2[sb] = 1
            else:
                d2[sb] += 1
        for k in d1:
            if k not in d2 and d1[k] == 1:
                res.append(k)
        for k in d2:
            if k not in d1 and d2[k] == 1:
                res.append(k)
        return res