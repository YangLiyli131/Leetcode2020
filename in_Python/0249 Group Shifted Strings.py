class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        hm = {}
        for x in strings:
            key = ()
            for i in range(1, len(x)):
                diff = (ord(x[i]) - ord(x[i-1])) % 26
                key += (diff,)
            if key not in hm:
                hm[key] = [x]
            else:
                hm[key].append(x)
        return hm.values()