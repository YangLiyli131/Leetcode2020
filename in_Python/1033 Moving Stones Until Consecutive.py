class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        n = [a,b,c]
        n.sort()
        x = n[0]
        y = n[1]
        z = n[2]
        mini = -1
        if x + 1 == y and y + 1 == z:
            mini = 0
        elif y - x > 2 and z - y > 2:
            mini = 2
        else:
            mini = 1
        maxi = z - x - 2
        return [mini, maxi]
        