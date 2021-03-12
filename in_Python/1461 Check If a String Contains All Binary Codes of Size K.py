class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        d = set()
        i = k
        while i <= len(s):
            cur = s[i-k:i]
            d.add(cur)
            i += 1
        return len(d) == 2**k