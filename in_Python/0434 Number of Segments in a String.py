class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        res = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1
        j = i
        while j < n:
            while j < n and s[j] != ' ':
                j += 1
            res += 1
            if j == n:
                return res
            i = j
            while i < n and s[i] == ' ':
                i += 1
            j = i
        return res