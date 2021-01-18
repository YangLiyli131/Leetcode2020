class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        res = {}
        n = len(s)
        l = minSize
        for i in range(l-1, n):
            sstr = s[i - l + 1 : i+1]
            cc = set(list(sstr))
            if len(cc) <= maxLetters:
                if sstr not in res:
                    res[sstr] = 1
                else:
                    res[sstr] += 1
        if not res:
            return 0
        return max(res.values())


class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        res = {}
        n = len(s)
        for l in range(minSize, maxSize+1):
            for i in range(l-1, n):
                sstr = s[i - l + 1 : i+1]
                cc = set(list(sstr))
                if len(cc) <= maxLetters:
                    if sstr not in res:
                        res[sstr] = 1
                    else:
                        res[sstr] += 1
        if not res:
            return 0
        return max(res.values())