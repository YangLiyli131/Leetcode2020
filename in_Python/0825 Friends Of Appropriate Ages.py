class Solution(object):
    def check(self, a,b):
        if a <= 0.5 * b + 7 or a > b:
            return False
        return True
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        res = 0
        d = {}
        for a in ages:
            if a not in d:
                d[a] = 1
            else:
                d[a] += 1
        for k1 in d:
            for k2 in d:
                if self.check(k1,k2):
                    x = d[k1]
                    y = d[k2]
                    if k1 == k2:
                        y -= 1
                    res += x * y
        return res