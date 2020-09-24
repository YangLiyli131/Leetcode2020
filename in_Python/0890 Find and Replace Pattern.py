class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for w in words:
            d = {}
            flag = True
            for i in range(len(pattern)):
                k = pattern[i]
                v = w[i]
                if k not in d and v in d.values():
                    flag = False
                    break
                if k in d and d[k] != v:
                    flag = False
                    break
                if k not in d:
                    d[k] = v
                
            if flag:
                res.append(w)
        return res