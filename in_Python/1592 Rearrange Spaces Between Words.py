class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        ts = text.split(' ')
        words = []
        numwords = 0
        for x in ts:
            if x != '':
                numwords += len(x)
                words.append(x)
        num = len(text) - numwords
        lw = len(words)
        if lw == 1:
            res = words[0]
            while num != 0:
                num -= 1
                res += ' '
            return res
        spaces = num / (lw-1)
        rd = num % (lw-1)
        res = ''
        for w in words[:-1]:
            res += w
            p = spaces
            while p != 0:
                p -= 1
                res += ' '
        res += words[-1]
        while rd != 0:
            rd -= 1
            res += ' '
        return res