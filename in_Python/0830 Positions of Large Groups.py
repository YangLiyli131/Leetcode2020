class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        i = 0
        j = 0
        res = []
        while j < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            if (j-i) >= 3:
                res.append([i,j-1])
            i = j
        return res
                         