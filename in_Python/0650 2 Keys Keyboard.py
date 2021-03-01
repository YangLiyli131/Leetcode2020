class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = {}
        d[1] = 0
        if n == 1:
            return 0
        i = 2
        while i <= n:
            if i % 2 != 0:
                kys = d.keys()
                kys.sort(reverse = True)
                for k in kys:
                    if i % k == 0:
                        d[i] = i/k + d[k]
                        break
            else:
                cur = d[i/2] + 2
                d[i] = cur
            i += 1
        return d[n]