class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        d = {}
        for i in range(len(S)):
            cur = S[i]
            if cur not in d:
                d[cur] = [i]
            else:
                d[cur].append(i)
        for w in words:
            minim = -1
            for c in w:
                if c not in d:
                    minim = -1
                    break
                for i in d[c]:
                    found = 0
                    if i > minim:
                        minim = i
                        found = 1
                        break
                if found == 0:
                    minim = -1
                    break
            if minim != -1:
                count += 1
        return count
                    