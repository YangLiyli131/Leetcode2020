class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = []
        for c in s:
            if c == '(':
                st.append(c)
            elif c != ')':
                st.append(c)
            else:
                temp = []
                while len(st) != 0 and st[-1] != '(':
                    temp.append(st.pop())
                if len(st) != 0:
                    st.pop()
                for t in temp:
                    st.append(t)
        res = ''
        for i in st:
            res += i
        return res
            
        