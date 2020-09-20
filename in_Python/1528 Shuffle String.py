class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        dict = {}
        for i in range(len(indices)):
            dict[indices[i]] = i
        res = ''
        indices.sort()
        for i in indices:
            res += s[dict[i]]
        return res

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res = []
        for i in range(len(s)):
            res.append('a')
        for i in range(len(s)):
            res[indices[i]] = s[i]
        result = ''
        for r in res:
            result += r
        return result