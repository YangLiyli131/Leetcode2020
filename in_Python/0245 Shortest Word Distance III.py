class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res = sys.maxint
        if word1 == word2:
            idx = []
            for i in range(len(words)):
                if words[i] == word1:
                    idx.append(i)
                    if len(idx) > 1:
                        res = min(res, idx[-1] - idx[-2])
            return res
        i, j = -1, -1
        for idx in range(len(words)):
            if words[idx] == word1:
                i = idx
                if j != -1:
                    res = min(res, abs(j-i))
            if words[idx] == word2:
                j = idx
                if i != -1:
                    res = min(res, abs(j-i))
        return res
                    
        