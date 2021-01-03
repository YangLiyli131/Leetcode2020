class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        d = collections.Counter(deliciousness)
        res = 0
        keys = d.keys()
        seen = set()
        for i in range(len(keys)):
            a = keys[i]
            for p in range(22):
                if (pow(2, p) - a) in d:
                    b = pow(2, p) - a
                    if (a,b) not in seen and (b,a) not in seen:
                        seen.add((a,b))
                        seen.add((b,a))
                        if a == b:
                            res += d[a] * (d[a]-1) /2
                        else:
                            res += d[a] * d[b]
        return res % (pow(10, 9) + 7)