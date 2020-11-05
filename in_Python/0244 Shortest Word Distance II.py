class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.d = {}
        for i in range(len(words)):
            cur = words[i]
            if cur not in self.d:
                self.d[cur] = [i]
            else:
                self.d[cur].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        x = self.d[word1]
        y = self.d[word2]
        res = sys.maxint
        for xi in x:
            for yi in y:
                res = min(res, abs(xi-yi))
                if res == 1:
                    return res
        return res
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)


class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.d = {}
        for i in range(len(words)):
            cur = words[i]
            if cur not in self.d:
                self.d[cur] = [i]
            else:
                self.d[cur].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        x = self.d[word1]
        y = self.d[word2]
        res = sys.maxint
        i,j = 0,0
        while i < len(x) and j < len(y):
            res = min(res, abs(x[i] - y[j]))
            if x[i] < y[j]:
                i += 1
            else:
                j += 1
        return res
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)