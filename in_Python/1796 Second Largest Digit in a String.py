class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = collections.Counter(s)
        f,s = -1,-1
        for idx in range(9,-1,-1):
            i = str(idx)
            if i not in d:
                continue
            if f == -1:
                f = i
            elif f != -1:
                s = i
            if s != -1:
                break
        return s