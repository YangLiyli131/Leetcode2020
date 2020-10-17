class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        d = {}
        for x in p:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        i,j = 0,0
        counter = len(d)
        while j < len(s):
            cur = s[j] 
            if cur in d:
                d[cur] -= 1
                if d[cur] == 0:
                    counter -= 1
            j += 1
            while counter == 0:
                first = s[i]
                if first in d:
                    d[first] += 1
                    if d[first] > 0:
                        counter += 1
                if j - i == len(p):
                    res.append(i)
                i += 1
        return res