class Solution(object):
    def lastIndex(self, S, c):
        for i in range(len(S)-1, -1, -1):
            if S[i] == c:
                return i
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        i = 0
        while i < len(S):
            ch = S[i]
            j = self.lastIndex(S,ch)
            idx = i
            while idx < j:
                #print(self.lastIndex(S, S[idx]))
                j = max(j, self.lastIndex(S, S[idx]))
                idx += 1
            #print(j)
            res.append(j-i+1)
            i = j+1
        return res
        