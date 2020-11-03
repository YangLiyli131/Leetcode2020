class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        N = len(s)
        for i in range(1, N/2 +1):
            if N % 2 == 1 and i % 2 == 0:
                continue
            if N % i != 0:
                continue
            ss = s[0:i]
            j = i + i
            check = 0
            while j <= len(s):
                nx = s[(j-i) : j]
                if nx != ss:
                    check = 1
                    break
                j += i
            if check == 1:
                continue
            else:
                return True
        return False
            