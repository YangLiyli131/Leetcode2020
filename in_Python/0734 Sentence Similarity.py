class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2, similarPairs):
        """
        :type sentence1: List[str]
        :type sentence2: List[str]
        :type similarPairs: List[List[str]]
        :rtype: bool
        """
        if len(sentence1) != len(sentence2):
            return False
        d = {}
        for p in similarPairs:
            a = p[0]
            b = p[1]
            if a not in d:
                d[a] = [b]
            else:
                d[a].append(b)
            if b not in d:
                d[b] = [a]
            else:
                d[b].append(a)

        for i in range(len(sentence1)):
            x = sentence1[i]
            y = sentence2[i]
            if x == y:
                continue
            if x in d and y not in d[x]:
                return False
            if y in d and x not in d[y]:
                return False
        return True