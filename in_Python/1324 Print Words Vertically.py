class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        temp = []
        maxlen = 0
        for i in s.split(' '):
            if len(i) > maxlen:
                maxlen = len(i)
        t = s.split(' ')
        n = len(t)
        # temp shall be a maxlen-by-n matrix
        for i in range(maxlen):
            row = []
            for j in range(n):
                row.append(' ')
            temp.append(row)
            
        for idx in range(n):
            ss = t[idx]
            for r in range(len(ss)):
                temp[r][idx] = ss[r]
        res = []
        for row in range(maxlen):
            cur = temp[row]
            st = ""
            for c in cur:
                st += c
            res.append(st.rstrip())
        return res