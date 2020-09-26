class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        st = []
        for s in S:
            if s == '(':
                st.append(s)
            else:
                if len(st) != 0 and st[-1] == '(':
                    st.pop()
                    st.append(1)
                else:
                    cursum = 0
                    while len(st) != 0 and st[-1] != '(':
                        cursum += st.pop()
                    st.pop()
                    st.append(cursum * 2)
        res = 0
        while len(st) != 0:
            res += st.pop()
        return res
        