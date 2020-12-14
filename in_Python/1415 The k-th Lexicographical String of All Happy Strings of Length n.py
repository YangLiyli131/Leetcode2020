class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        level = 1
        base = ['a','b','c']
        while level != n:
            tmp = []
            for prev in base:
                if prev[-1] == 'a':
                    tmp.append(prev + 'b')
                    tmp.append(prev + 'c')
                elif prev[-1] == 'b':
                    tmp.append(prev + 'a')
                    tmp.append(prev + 'c')
                else:
                    tmp.append(prev + 'a')
                    tmp.append(prev + 'b')
            base = tmp
            level += 1   
        if len(base) < k:
            return ""
        return base[k-1]