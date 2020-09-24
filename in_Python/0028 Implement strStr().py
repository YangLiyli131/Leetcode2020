class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        l = len(needle)
        for i in range(len(haystack) - l + 1):
            s = haystack[i : i + l]
            if s == needle:
                return i
        return -1