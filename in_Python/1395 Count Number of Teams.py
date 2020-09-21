class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        res = 0
        l = len(rating)
        for i in range(l):
            for j in range(i+1, l):
                for k in range(j+1, l):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        res += 1
        return res