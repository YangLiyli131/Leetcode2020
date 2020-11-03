# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        can = 0
        for i in range(1, n):
            if knows(can,i):
                can = i
        for i in range(n):
            if i != can and (knows(can,i) or not knows(i,can)):
                return -1
        return can
            