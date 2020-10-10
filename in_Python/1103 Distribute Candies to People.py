class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        run = 0
        res = [0] * num_people
        remain = candies
        while remain > 0:
            for i in range(num_people):
                give = run * num_people + i + 1
                if give > remain:
                    res[i] += remain
                    remain -= give
                    break
                else:
                    res[i] += give
                    remain -= give
            run += 1
        return res