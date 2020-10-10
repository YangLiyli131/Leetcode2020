class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        i,j = 0,0
        groups = []
        while j < len(s):
            cur = s[i]
            while j < len(s) and s[j] == cur:
                j += 1
            groups.append(s[i:j])
            i = j
        res = 0
        for i in range(1, len(groups)):
            res += min(len(groups[i]), len(groups[i-1]))
        return res