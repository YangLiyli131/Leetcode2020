class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        d = {}
        for ss in s:
            if ss not in d:
                d[ss] = 1
            else:
                d[ss] += 1
        c = {}
        count = []
        for k in d:
            v = d[k]
            if v not in c:
                count.append(v)
                t = []
                t.append(k)
                c[v] = t
            else:
                t = c[v]
                t.append(k)
                c[v] = t
        count.sort()
        for i in range(len(count)-1, -1, -1):
            ct = count[i]
            arr = c[ct]
            arr.sort()
            for x in arr:
                num = ct
                while num != 0:
                    res += x
                    num -= 1
        return res
        