class Solution(object):
    def minimumSemesters(self, n, relations):
        """
        :type n: int
        :type relations: List[List[int]]
        :rtype: int
        """
        d = {}
        for i in range(n+1):
            d[i] = []
        dg = [0] * (n+1)
        res = dg[:]
        for x in relations:
            a,b = x[0], x[1]
            dg[b] += 1
            d[a].append(b)
        st = [i for i in range(len(dg)) if dg[i] == 0]
        for i in st:
            for j in d[i]:
                res[j] = max(res[j], res[i] + 1)
                dg[j] -= 1
                if dg[j] == 0:
                    st.append(j)
        if len(st) != n+1:
            return -1
        return max(res) + 1