class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        def removez(x):
            if x == '0':
                return x
            i = 0
            while i < len(x) and x[i] == '0':
                i += 1
            return x[i:]
        r = set()
        i = 0
        n = len(word)
        while i < n and not word[i].isdigit():
            i += 1
        while i < n:
            if not word[i].isdigit():
                i += 1
                continue
            j = i + 1
            while j < n and word[j].isdigit():
                j += 1
            cs = word[i : j]
            r.add(cs)
            i = j
        rr = set()
        for x in r:
            rr.add(removez(x))
        return len(rr)
            