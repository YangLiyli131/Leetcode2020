class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        st = []
        d = {}
        for k in knowledge:
            d[k[0]] = k[1]
        r = []
        show = 0
        for x in s:
            if x not in '()':
                if show == 0:
                    r.append(x)
                else:
                    st.append(x)
            elif x == '(':
                show = 1
            else:
                k = []
                while st and st[-1] != '(':
                    k.append(st.pop())
                k = k[::-1]
                k = ''.join(k)
                if k not in d:
                    r.append('?')
                else:
                    r.append(d[k])
                show = 0
        return ''.join(r)
                    