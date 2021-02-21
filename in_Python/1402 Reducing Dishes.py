class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        satisfaction.sort(reverse = True)
        r = []
        res = 0
        x = 0
        idx = 0
        while idx < len(satisfaction) and x + satisfaction[idx] > 0:
            x += sum(r) + satisfaction[idx]
            res = max(res,x)
            r.append(satisfaction[idx])
            idx += 1
        return res