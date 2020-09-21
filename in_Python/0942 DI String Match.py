class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        N = 0
        res = []
        for i in range(len(S)+1):
            res.append(0)
        D_id = []
        I_id = []
        for i in range(len(S)):
            if S[i] == 'I':
                I_id.append(i)
            else:
                D_id.append(i)
        for iid in I_id:
            res[iid] = N
            N += 1
        N = len(S)
        for did in D_id:
            res[did] = N
            N -= 1
        for i in range(len(S)+1):
            if i not in res:
                res[-1] = i
                break
        return res