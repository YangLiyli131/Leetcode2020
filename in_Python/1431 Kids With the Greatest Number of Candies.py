class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        cm = max(candies)
        res = []
        for i in range(len(candies)):
            candies[i] += extraCandies
            res.append(candies[i] >= cm)
        return res