class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        res = 0
        flip = 0
        L = [0] * len(target)
        for i in range(len(target)):
            left = L[i]
            right = int(target[i])
            if flip == 1:
                left = 1 - left
            if left != right:
                res += 1
                flip = 1 - flip
        return res