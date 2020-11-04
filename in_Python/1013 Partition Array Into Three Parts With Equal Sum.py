class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        total = sum(A)
        if total % 3 != 0:
            return False
        ave = total / 3
        cursum = 0
        i = 0
        counter = 0
        while i < len(A):
            cursum += A[i]
            if cursum == ave:
                counter += 1
                cursum = 0
            i += 1
        if ave == 0:
            return counter >= 3
        return counter == 3