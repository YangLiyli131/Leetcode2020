class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        base = list(range(1,10))
        res = []
        added = True
        while added:
            added = False
            cur = []
            for x in base:
                pre = x % 10
                if pre + 1 < 10:
                    added = True
                    y = x * 10 + pre + 1
                    cur.append(y)
                    if low <= y <= high:
                        res.append(y)
                else:
                    cur.append(x)
            base = cur
        return sorted(res)
                        
        