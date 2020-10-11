class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target < letters[0]:
            return letters[0]
        if target >= letters[-1]:
            return letters[0]
        i,j = 0, len(letters)-1
        while i < j:
            m = i + (j-i)/2
            if letters[m] > target:
                j = m
            else:
                i = m+1
        return letters[j]
        