class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        d = {'1':'1','6':'9','9':'6','0':'0','8':'8'}
        res = []
        x = list(num)
        while x:
            y = x.pop()
            if y not in d:
                return False
            res.append(d[y])
        xx = ''.join(res)
        return xx == num