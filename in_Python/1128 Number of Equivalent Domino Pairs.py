class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        d = {}
        for dm in dominoes:
            dm.sort()
            dm = str(dm[0]) + str(dm[1])
            if dm not in d:
                d[dm] = 1
            else:
                d[dm] += 1
        res = 0
        for k in d:
            num = d[k]
            res += num * (num-1) / 2
        return res