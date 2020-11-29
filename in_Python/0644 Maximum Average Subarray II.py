class Solution(object):
    def findMaxAverage(self, A, K):
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        if K < 100:
            ans = float('-inf')
            for k in xrange(K, min(2*K, N+1)):
                best_sum = max(P[i+k] - P[i] for i in xrange(N-k+1))
                ans = max(ans, best_sum / float(k))
            return ans

        def possible(x):
            m = P[0]
            for i, v in enumerate(P):
                m = min(m, v-i*x)
                if i+K == len(P): break
                if P[i+K] - (i+K)*x >= m:
                    return True
            return False

        lo, hi = min(A), max(A)
        while hi - lo > .00001:
            mi = (lo + hi) / 2.0
            if possible(mi):
                lo = mi
            else:
                hi = mi
        return lo