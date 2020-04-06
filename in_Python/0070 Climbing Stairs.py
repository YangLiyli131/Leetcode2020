class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = []
        temp.append(1)
        temp.append(1)
        for i in range(2,n+1):
            temp.append(temp[i-1]+temp[i-2])
        return temp[-1]