class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        num =  len(s) / (2*k)
        res = []
        start = 0
        end = 0
        for idx in range(num):
            start = idx * k * 2
            end = idx * k * 2 + k * 2 
            curs = s[start : end]
            thiscur = []
            for i in range(k):
                thiscur.insert(0, curs[i])
            for i in range(k, len(curs)):
                thiscur.append(curs[i])
            res.append(thiscur)
        thiscur = s[end : len(s)]
        newcur = []
        if len(thiscur) < k:
            for i in thiscur:
                newcur.insert(0,i)
        else:
            for i in range(k):
                newcur.insert(0, thiscur[i])
            for i in range(k, len(thiscur)):
                newcur.append(thiscur[i])
        res.append(newcur)
        r = ""
        for i in res:
            for j in i:
                r += j
        return r
            