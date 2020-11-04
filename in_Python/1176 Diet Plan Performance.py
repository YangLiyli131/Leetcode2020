class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        window = calories[0:k]
        total = sum(window)
        res = 0
        if total < lower:
            res -= 1
        if total > upper:
            res += 1
        i = 0
        j = k 
        while j < len(calories):
            total = total - calories[i] + calories[j]
            if total < lower:
                res -= 1
            if total > upper:
                res += 1
            i += 1
            j += 1
        return res
            