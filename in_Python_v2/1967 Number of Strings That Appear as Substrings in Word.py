class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        res = 0
        lists = []
        for i in range(len(word)):
            for j in range(i+1, len(word)+1):
                lists.append(word[i:j])
        for x in patterns:
            if x in lists:
                res += 1
        return res