class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        N = len(code)
        res = [0] * N
        if k == 0:
            return res
        elif k > 0:
            for i in range(N):
                cur = 0
                t = k
                while t != 0:
                    cur += code[(i+t) % N]
                    t -= 1
                res[i] = cur
        else:
            for i in range(N-1, -1, -1):
                cur = 0
                t = k
                while t != 0:
                    cur += code[i+t]
                    t += 1
                res[i] = cur
        return res
                