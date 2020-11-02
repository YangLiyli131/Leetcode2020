class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        d1 = {}
        for si in range(len(S)):
            d1[si] = S[si]
        d2 = {}
        for t in T:
            if t not in d2:
                d2[t] = 1
            else:
                d2[t] += 1
        res = []
        keys = d1.keys()
        keys.sort()
        for k in keys:
            letter = d1[k]
            if letter not in d2:
                continue
            num = d2[letter]
            while num != 0:
                num -= 1
                res.append(letter)
        for k in d2:
            if k not in d1.values():
                num = d2[k]
                while num != 0:
                    num -= 1
                    res.append(k)
        return ''.join(res)