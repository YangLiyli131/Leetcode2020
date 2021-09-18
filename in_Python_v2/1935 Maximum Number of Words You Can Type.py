class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        res = 0
        for x in text.split(' '):
            f = 1
            for y in brokenLetters:
                if y in x:
                    f = 0
                    break
            if f == 1:
                res += 1
        return res