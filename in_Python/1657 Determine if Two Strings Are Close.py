class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False
        word1 = ''.join(sorted(word1)) 
        word2 = ''.join(sorted(word2)) 
        if word1 == word2:
            return True
        count1 = collections.Counter(word1)
        count2 = collections.Counter(word2)
        k1 = count1.keys()
        k2 = count2.keys()
        for k in k2:
            if k not in k1:
                return False
        v1 = count1.values()
        v2 = count2.values()
        v1.sort()
        v2.sort()
        for i in range(len(v1)):
            if v1[i] != v2[i]:
                return False
        return True
        