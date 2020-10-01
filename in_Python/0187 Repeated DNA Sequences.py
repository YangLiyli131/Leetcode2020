class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = {}
        for i in range(len(s)):
            j = i + 10
            if j <= len(s):
                ss = s[i:j]
                if ss in d:
                    d[ss] += 1
                else:
                    d[ss] = 1
        res = []
        for k in d:
            if d[k] > 1:
                res.append(k)
        return res