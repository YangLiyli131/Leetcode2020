class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        d = {}
        for x in s1:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        i,j = 0,0
        counter = len(d)
        while j < len(s2):
            cur = s2[j]
            if cur in d:
                d[cur] -= 1
                if d[cur] == 0:
                    counter -= 1
            j += 1
            while counter == 0:
                first = s2[i]
                if first in d:
                    d[first] += 1
                    if d[first] > 0:
                        counter += 1
                if j - i == len(s1):
                    return True
                i += 1
        return False