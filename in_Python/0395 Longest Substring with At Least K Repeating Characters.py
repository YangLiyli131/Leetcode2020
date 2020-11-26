class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        d = collections.Counter(s)
        for si in d:
            if d[si] < k:
                return max(self.longestSubstring(t, k) for t in s.split(si))
        return len(s)