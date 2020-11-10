class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        d = collections.Counter(deck)
        val = d.values()
        mini = min(val)
        divisor = []
        for i in range(1, mini + 1):
            valid = 1
            for v in val:
                if v % i != 0:
                    valid = 0
                    break
            if valid == 1:
                divisor.append(i)
        if max(divisor) >= 2:
            return True
        return False
        