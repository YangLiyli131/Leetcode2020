class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        d = {}
        for i, k in enumerate(keyboard):
            d[k] = i
        res = d[word[0]]
        for i in range(1, len(word)):
            pre = d[word[i-1]]
            cur = d[word[i]]
            res += abs(pre- cur)
        return res