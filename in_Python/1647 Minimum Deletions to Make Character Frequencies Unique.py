class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for x in s:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        res = 0
        unique = set()
        dup = []
        for v in d.values():
            if v not in unique:
                unique.add(v)
            else:
                dup.append(v)
        for x in dup:
            while x in unique and x != 0:
                x -= 1
                res += 1
            if x != 0:
                unique.add(x)
        return res
                    
            
        