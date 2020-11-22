class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        A,B = tomatoSlices, cheeseSlices
        res = []
        a = A - 2 * B
        b = 4 * B - A
        if a % 2 != 0 or b % 2 != 0:
            return res
        if a < 0 or b < 0:
            return res
        return [a/2, b/2]
        