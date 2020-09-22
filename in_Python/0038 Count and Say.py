class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        res.append('1')
        if n == 1:
            return res[0]
        for idx in range(1, n):
            prev = res[idx-1]
            #print(prev)
            cur = ''
            L = prev
            i = 0
            while i < len(L):
                j = i+1
                while j < len(L) and L[j] == L[i]:
                    j += 1
                d = j - i 
                cur += str(d) + L[i]
                i = j
            res.append(cur)
        return res[-1]
                