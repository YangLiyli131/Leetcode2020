class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        res = 1
        cur = 0
        for s in S:
            w = widths[ord(s) - ord('a')]
            if cur + w <= 100:
                cur += w
            else:
                res += 1
                cur = w
        return [res, cur]