class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        base = 'abcdefghijklmnopqrstuvwxyz'
        res = []
        while 26 * (n-1) >= k:
            res.append('a')
            n -= 1
            k -= 1
        post = []
        while k > 26:
            post.append('z')
            k -= 26
        if k != 0:
            post.append(base[k-1])
        res += post[::-1]
        return ''.join(res)