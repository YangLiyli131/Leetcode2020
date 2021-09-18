class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = collections.Counter(s)
        v = d.values()
        vv = set(v)
        return len(vv) == 1
        