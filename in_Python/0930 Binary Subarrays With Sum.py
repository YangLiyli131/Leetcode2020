class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        if A == None or len(A) == 0:
            return 0
        d = {}
        res = 0
        d[A[0]] = [0]
        for i in range(1, len(A)):
            cur = A[i] + A[i-1]
            if cur not in d:
                t = [i]
                d[cur] = t
            else:
                t = d[cur]
                t.append(i)
                d[cur] = t
            A[i] = cur
        if S in d:
            res += len(d[S])
        if S == 0:
            for k in d:
                n = len(d[k])
                res += n * (n-1) / 2
        else:
            for k in d:
                if k + S in d:
                    a = d[k]
                    b = d[k+S]
                    for x in a:
                        for y in b:
                            if x < y:
                                res += 1
        return res