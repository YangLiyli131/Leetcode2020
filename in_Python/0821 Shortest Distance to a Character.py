class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        c_id = []
        for i in range(len(S)):
            if S[i] == C:
                c_id.append(i)
        res = []
        for i in range(len(S)):
            res.append(len(S))
        for cid in c_id:
            for i in range(len(res)):
                res[i] = min(res[i], abs(cid-i))
        return res
        