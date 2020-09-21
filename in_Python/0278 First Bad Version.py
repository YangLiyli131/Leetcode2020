# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        j = n
        while i < j:
            m = i + (j-i)/2
            if not isBadVersion(m):
                i = m + 1
            else:
                j = m
        return i