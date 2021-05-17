class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = {}
        words = sorted(words, key = lambda x : len(x))
        res = 1
        for w in words:
            cur = 1
            for i in range(len(w)):
                nw = w[:i] + w[i+1:]
                pre = 0
                if nw in d:
                    pre = d[nw]
                cur = max(cur, pre+1)
            d[w] = cur
            res = max(res, cur)
        return res