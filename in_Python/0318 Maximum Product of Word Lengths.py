class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        counter = {}
        for w in words:
            L = len(w)
            x = [ch for ch in w]
            x = set(x)
            cur = []
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c in x:
                    cur.append(1)
                else:
                    cur.append(0)
            cur = tuple(cur)
            if cur not in counter:
                counter[cur] = L
            else:
                counter[cur] = max(counter[cur], L)
        res = 0
        keys = counter.keys()
        def check(a, b):
            i = 0
            while i < len(a):
                if a[i] == 1 and b[i] == 1:
                    return False
                i += 1
            return True
        
        for i in range(len(keys)):
            k1 = keys[i]
            for j in range(i+1, len(keys)):
                k2 = keys[j]
                if check(k1, k2):
                    res = max(res, counter[k1] * counter[k2])
        return res