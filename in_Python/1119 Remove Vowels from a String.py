class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = []
        for i in S:
            if i not in ['a','e','i','o','u']:
                res.append(i)
        return ''.join(res)