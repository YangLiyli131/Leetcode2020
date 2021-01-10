class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        bt = [[]]
        for s in S:
            cur = []
            if '0' <= s <= '9':
                for pre in bt:
                    pre += [s]
                    cur.append(pre)
            else:
                for pre in bt:
                    pree = pre[:]
                    pre += [s]
                    if 'a' <= s <= 'z':
                        pree += [s.upper()]
                    else:
                        pree += [s.lower()]
                    cur.append(pre)
                    cur.append(pree)
            bt = cur
        for x in bt:
            res.append(''.join(x))
        return res
            