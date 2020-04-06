class Solution(object):
    def freq(self,s):
        t = sorted(list(s))
        t = t[0]
        res = 0
        for i in list(s):
            if i == t:
                res += 1
        return res
        
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        t1 = []
        t2 = []
        for i in queries:
            t1.append(self.freq(i))
        for i in words:
            t2.append(self.freq(i))
        t3 = sorted(t2)
        res = []
        for x in t1:
            flag = True
            for y in range(len(t3)):
                if t3[y] > x:
                    flag = False 
                    break
            if flag:
                res.append(0)
            else:
                res.append(len(t3)-y)
        return res