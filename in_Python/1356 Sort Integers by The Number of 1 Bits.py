class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        c = []
        d = {}
        for num in arr:
            n = num
            count = 0
            while num != 0:
                count += num % 2
                num /= 2
            if count not in c:
                c.append(count)
            if count not in d:
                t = []
                t.append(n)
                d[count] = t
            else:
                t = d[count]
                t.append(n)
                d[count] = t
        c.sort()
        res = []
        for cc in c:
            ns = d[cc]
            ns.sort()
            for j in ns:
                res.append(j)
        return res
        