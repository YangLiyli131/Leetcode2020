class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        res = ''
        s = sentence.split(' ')
        for si in s:
            j = 1
            loc = 0
            while j <= len(si):
                if si[0:j] in dictionary:
                    loc = 1
                    break
                j += 1
            if loc == 1:
                res += si[0:j]
            else:
                res += si
            res += ' '
        return res.strip()
                