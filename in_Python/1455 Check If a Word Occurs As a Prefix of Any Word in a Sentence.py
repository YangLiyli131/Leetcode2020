class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        L = sentence.split(' ')
        for idx in range(len(L)):
            i = L[idx]
            if len(i) < len(searchWord):
                continue
            if i[0: len(searchWord)] == searchWord:
                return idx+1
        return -1