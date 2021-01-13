class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        res = 0
        people.sort()
        i,j = 0, len(people) - 1
        while i < j:
            if people[i] + people[j] <= limit:
                res += 1
                i += 1
                j -= 1
            elif people[i] + people[j] > limit:
                res += 1
                j -= 1
        if i == j:
            res += 1
        return res
        