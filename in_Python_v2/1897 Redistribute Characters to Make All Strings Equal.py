class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        n = len(words)
        d = {}
        for w in words:
            for x in w:
                if x not in d:
                    d[x] = 0
                d[x] += 1
        for x in d:
            if d[x] % n != 0:
                return False
        return True