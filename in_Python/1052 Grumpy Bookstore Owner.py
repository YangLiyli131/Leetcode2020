class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        res = 0
        happy = 0
        maxturned = 0
        turned = 0
        idx = 0
        for i in range(len(customers)):
            happy += customers[i] * (1 - grumpy[i])
            turned += customers[i] * grumpy[i]
            if i >= X:
                turned -= customers[i-X] * grumpy[i-X]
            maxturned = max(maxturned, turned)
        return happy + maxturned