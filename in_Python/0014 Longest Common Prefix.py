class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if strs == None or len(strs) == 0:
            return res
        minlen = len(strs[0])
        mins = strs[0]
        for i in range(1, len(strs)):
            if len(strs[i]) < minlen:
                minlen = len(strs[i])
                mins = strs[i]
        for i in range(minlen):
            cur_c = mins[i]
            for sts in strs:
                if sts[i] != cur_c:
                    return res
            res += cur_c
        return res