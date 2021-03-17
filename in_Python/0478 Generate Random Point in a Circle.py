import random
class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        f = True
        while f:
            a = random.uniform(self.x - self.r, self.x + self.r)
            b = random.uniform(self.y - self.r, self.y + self.r)
            if (a-self.x)**2 + (b-self.y)** 2 <= self.r ** 2:
                f = False
                r0 = a
                r1 = b
        return [r0,r1]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()