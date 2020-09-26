class Solution(object):
    def isLetter(self, l):
        if l >= 'a' and l <= 'z':
            return True
        if l >= 'A' and l <= 'Z':
            return True
        return False
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        d = {}
        res = ''
        for x in licensePlate:
            if self.isLetter(x):
                x = x.lower()
                if x not in d:
                    d[x] = 1
                else:
                    d[x] += 1
        for w in words:
            found = True
            dw = {}
            for wi in w:
                wi = wi.lower()
                if wi not in dw:
                    dw[wi] = 1
                else:
                    dw[wi] += 1
            for k in d:
                if k not in dw:
                    found = False
                    break
                if d[k] > dw[k]:
                    found = False
                    break
            if found:
                if res == '':
                    res = w
                else:
                    if len(res) > len(w):
                        res = w
        return res