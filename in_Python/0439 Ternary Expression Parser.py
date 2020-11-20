class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        st = []
        i = len(expression)-1
        while i >= 0:
            x = expression[i]
            if x != '?':
                if x != ':':
                    st.append(x)
                i -= 1
            else:
                flag = expression[i-1]
                a = st.pop()
                b = st.pop()
                if flag == 'T':
                    st.append(a)
                else:
                    st.append(b)
                i -= 2
        return st[0]
                    