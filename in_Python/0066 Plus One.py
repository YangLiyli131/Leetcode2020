class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        j = len(digits) - 1
        digits[j] += 1
        c = 0
        while j >= 0:
            cn = digits[j] + c 
            digits[j] = cn % 10
            c = cn / 10
            j -= 1
        if c == 1:
            digits.insert(0,1)
        return digits