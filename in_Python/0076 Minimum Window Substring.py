class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        i,j = 0,0
        d = {}
        for x in t:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        res = ""
        L = len(t)
        while j < len(s):
            cur = s[j]
            if cur in d and d[cur] > 0:
                L -= 1
            if cur not in d:
                d[cur] = -1
            else:
                d[cur] -= 1
            while L == 0:
                if res == "":
                    res = s[i: (j+1)]
                else:
                    if len(res) > j-i+1:
                        res = s[i: (j+1)]
                d[s[i]] += 1
                if d[s[i]] > 0:
                    L += 1
                i += 1
            j += 1
        return res
        