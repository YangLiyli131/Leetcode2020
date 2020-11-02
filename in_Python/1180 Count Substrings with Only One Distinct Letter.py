class Solution(object):
    def countLetters(self, S):
        """
        :type S: str
        :rtype: int
        """
        res = 0
        i,j = 0,0
        while j < len(S):
            while j < len(S) and S[j] == S[i]:
                j += 1
            L = j - i
            res += L * (L+1) / 2
            i = j
        return res