class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s.split(' ')
        res = [''] * len(arr)
        for x in arr:
            idx = int(x[-1]) - 1
            res[idx] = x[:-1]
        return ' '.join(res)