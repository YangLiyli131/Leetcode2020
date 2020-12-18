class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        fir = sec = sys.maxint
        for n in nums:
            if n <= fir:
                fir = n
            elif n <= sec:
                sec = n
            else:
                return True
        return False
                
                
        