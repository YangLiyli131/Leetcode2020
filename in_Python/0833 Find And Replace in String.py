class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        if S == None or len(S) == 0:
            return S
        temp = []
        i = 0
        while i < len(S):
            if i in indexes:
                idx = indexes.index(i)
                source = sources[idx]
                if i + len(source) <= len(S) and source == S[i:(i + len(source))]:
                    temp.append(targets[idx])
                    i += len(source)
                else:
                    temp.append(S[i])
                    i += 1
            else:
                temp.append(S[i])
                i += 1
        #print(temp)
        return ''.join(temp)
                