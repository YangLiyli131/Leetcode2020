class Solution(object):
    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        st = []
        for s in S:
            if s != '}':
                st.append(s)
            else:
                cur = []
                while st and st[-1] != '{':
                    tmp = st.pop()
                    if tmp != ',':
                        cur.insert(0,tmp)
                st.pop()
                st.append(''.join(cur))
        res = ['']
        for part in st:
            newres = []
            for x in part:
                for y in res:
                    newres.append(y+x)
            res = newres
        res.sort()
        return res