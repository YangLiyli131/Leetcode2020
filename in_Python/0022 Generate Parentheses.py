class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        L = [['(',1,0]]
        res = []
        added = True
        while added:
            added = False
            cur = []
            for pre in L:
                s = pre[0]
                l = pre[1]
                r = pre[2]
                if l > r and l != n:
                    added = True
                    cur.append([s + '(', l+1, r])
                    cur.append([s + ')', l, r+1])
                elif l > r and l == n:
                    xs = s
                    while r != n:
                        xs += ')'
                        r += 1
                    added = True
                    cur.append([xs,n,n])
                elif l == r and l != n:
                    added = True
                    cur.append([s + '(', l+1, r])
                elif l == r and l == n:
                    cur.append([s,n,n])
            if len(cur) == 0:
                break
            L = cur
        for x in L:
            res.append(x[0])
        return res