class Solution(object):
    def isS(self, x,y):
        if x == y:
            return True
        n = len(y)
        for i in range(len(x)-n+1):
            if x[i:i+n] == y:
                return True
        return False
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        k = 0
        if not self.isS(sequence, word):
            return k
        k = 1
        w = word
        while self.isS(sequence, w):
            k += 1
            w = word * k
        return k-1