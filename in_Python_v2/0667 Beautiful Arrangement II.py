class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = []
        for i in range(1, n - k):
            res.append(i)
        t = list(range(n-k, n+1))
        i,j = 0, len(t)-1
        while i < j:
            res.append(t[i])
            res.append(t[j])
            i += 1
            j -= 1
        if i == j:
            res.append(t[i])
        return res
            