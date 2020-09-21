class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(A)):
            res.append(0)
        i = 0
        j = -1
        for a in A:
            if a % 2 == 0:
                res[i] = a
                i += 1
            else:
                res[j] = a
                j -= 1
        return res
                