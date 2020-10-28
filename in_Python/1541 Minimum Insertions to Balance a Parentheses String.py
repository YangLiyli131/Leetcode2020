class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        res = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                st.append(s[i])
                i += 1
            elif i+2 <= len(s) and s[i : (i+2)] == '))':
                if len(st) == 0:
                    res += 1
                else:
                    st.pop()
                i += 2
            else:
                if len(st) == 0:
                    res += 2
                else:
                    res += 1
                    st.pop()
                i += 1
        while st:
            st.pop()
            res += 2
        return res