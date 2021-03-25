class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        A = map(set, languages)
        res = sys.maxint
        for k in xrange(1, n + 1):
            teach = set()
            for i, j in friendships:
                if A[i - 1] & A[j - 1]: continue
                if k not in A[i - 1]: teach.add(i)
                if k not in A[j - 1]: teach.add(j)
            res = min(res, len(teach))
        return res