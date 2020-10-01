class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = two = three = -sys.maxint
        for i in nums:
            if i > one:
                one, two, three = i, one, two
            elif i < one and i > two:
                two, three = i, two
            elif i < two and i > three:
                three = i
        return three if three != -sys.maxint else one