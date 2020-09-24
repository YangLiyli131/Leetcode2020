class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words.sort(key = len)
        res = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    if words[i] not in res:
                        res.append(words[i])
        return res