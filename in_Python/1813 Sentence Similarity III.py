class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        s1 = sentence1.split(' ')
        s2 = sentence2.split(' ')
        if len(s1) == len(s2):
            return sentence1 == sentence2
        if len(s1) < len(s2):
            sh = s1
            lo = s2
        else:
            sh = s2
            lo = s1
        d = {}
        for i,x in enumerate(lo):
            if x not in d:
                d[x] = []
            d[x].append(i)
        res = []
        for x in sh:
            if x not in d:
                return False
            row = d[x]
            if len(row) == 0:
                return False        
            res.append(row.pop(0))
            d[x] = row
            if len(row) == 0:
                d.pop(x, None)
        gap = 0
        #print(res)
        if res[0] != 0:
            gap += 1
        if res[-1] != len(lo)-1:
            gap += 1
        if gap > 1:
            return False
        for i in range(1, len(res)):
            if res[i] != res[i-1]+1:
                gap += 1
                if gap > 1:
                    return False
        return True
        