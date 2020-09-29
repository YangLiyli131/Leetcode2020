class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        d = {}
        d[5] = 0
        d[10] = 0
        for i in bills:
            if i == 5:
                d[5] += 1
            elif i == 10:
                d[10] += 1
                if d[5] == 0:
                    return False
                else:
                    d[5] -= 1
            else:
                if d[10] != 0:
                    d[10] -= 1
                    if d[5] != 0:
                        d[5] -= 1
                    else:
                        return False
                else:
                    if d[5] < 3:
                        return False
                    else:
                        d[5] -= 3
        return True