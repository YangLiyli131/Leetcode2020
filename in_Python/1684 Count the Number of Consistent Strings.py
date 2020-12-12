class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        res = 0
        l = set()
        for s in allowed:
            l.add(s)
        for w in words:
            f = 0
            for wi in w:
                if wi not in l:
                    f = 1
                    break
            if f == 0:
                res += 1
        return res