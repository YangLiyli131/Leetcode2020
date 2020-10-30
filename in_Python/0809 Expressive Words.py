class Solution(object):
    def split(self, s):
        res = []
        i = 0
        j = 0
        while j < len(s):
            while j < len(s) and s[j] == s[i]:
                j += 1
            res.append(s[i:j])
            i = j
        return res
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        res = 0
        slist = self.split(S)
        for w in words:
            ww = self.split(w)
            if len(ww) != len(slist):
                continue
            match = 1
            for i in range(len(ww)):
                a = ww[i]
                b = slist[i]
                if a[0] != b[0] or len(a) > len(b):
                    match = 0
                    break
                if len(a) == len(b):
                    continue
                if len(a) < len(b) and len(b) < 3:
                    match = 0
                    break
            if match == 1:
                res += 1
        return res