class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        res = []
        dict = {}
        for i in range(26):
            dict[chr(ord('a')+i)] = 101
        for s in A:
            newdict = {}
            for i in range(26):
                newdict[chr(ord('a')+i)] = 0
            for c in list(s):
                newdict[c] += 1
            for k in newdict:
                if newdict[k] < dict[k]:
                    dict[k] = newdict[k]
        for k in dict:
            n = dict[k]
            while n != 0:
                res.append(k)
                n -= 1
        return res
        