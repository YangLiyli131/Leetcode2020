class Solution(object):
    def numKLenSubstrNoRepeats(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: int
        """
        if K > len(S):
            return 0
        res = 0
        i,j = 0, K-1
        d = {}
        for x in range(K):
            if S[x] not in d:
                d[S[x]] = 1
            else:
                d[S[x]] += 1
        if len(d) == K:
            res = 1
        i += 1
        j += 1
        while j < len(S):
            pre = S[i-1]
            cur = S[j]
            d[pre] -= 1
            if d[pre] == 0:
                d.pop(pre, None)
            if cur not in d:
                d[cur] = 1
            else:
                d[cur] += 1
            if len(d) == K:
                res += 1
            i += 1
            j += 1
        return res