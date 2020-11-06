class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        i = 2
        while i <= len(s):
            pre = s[:i-2]
            cur = s[i-2 : i]
            nex = s[i:]
            if cur == '++':
                res.append(pre + '--' + nex)
            i += 1
        return res
            