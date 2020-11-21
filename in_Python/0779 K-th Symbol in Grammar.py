class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        k = K-1
        ops = []
        while N != 1:
            if k % 2 != 0:
                ops.append(-1)
            else:
                ops.append(1)
            k /= 2
            N -= 1
        res = 0
        while ops:
            op = ops.pop()
            if op == -1:
                res = 1 - res 
        return res