class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        r = []
        i,j = 0,0
        idx = 0
        while i < len(word1) and j < len(word2):
            if idx % 2 == 0:
                r.append(word1[i])
                i += 1
            else:
                r.append(word2[j])
                j += 1
            idx += 1
        while i < len(word1):
            r.append(word1[i])
            i += 1
        while j < len(word2):
            r.append(word2[j])
            j += 1
        return ''.join(r)