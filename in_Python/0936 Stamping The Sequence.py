class Solution(object):
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        n, m = len(stamp), len(target)
        s, t = list(stamp), list(target)
        res = []
        
        def check(i):
            changed = False
            for j in range(n):
                if t[i+j] == '?':
                    continue
                if t[i+j] != s[j]:
                    return False
                changed = True
            if changed:
                t[i: i+n] = ['?'] * n
                res.append(i)
            return changed
        c = True
        while c:
            c = False
            for i in range(m - n + 1):
                tp = check(i)
                c = c | tp
        if t == ['?'] * m:
            return res[::-1]
        return []