class Solution(object):
    def dsum(self, i):
        res = 0
        for s in str(i):
            res += ord(s) - ord('0')
        return res
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        dict = {}
        maxcount = 1
        for i in range(1, n+1):
            x = self.dsum(i)
            #print(x)
            if x not in dict:
                dict[x] = 1
            else:
                count = dict[x]
                count += 1
                if count > maxcount:
                    maxcount = count
                dict[x] = count
        res = 0
        for k in dict:
            if dict[k] == maxcount:
                res += 1
        return res
        