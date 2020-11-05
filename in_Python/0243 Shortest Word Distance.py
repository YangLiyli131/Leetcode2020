class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res = len(words)
        id1 = -1
        id2 = -1
        for i in range(len(words)):
            cur = words[i]
            if cur == word1:
                id1 = i
                if id2 != -1:
                    res = min(res, abs(id1 - id2))
            elif cur == word2:
                id2 = i
                if id1 != -1:
                    res = min(res, abs(id1 - id2))
        return res
        