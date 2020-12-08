class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        st = []
        for s in S:
            if s == '(':
                st.append(s)
            else:
                if len(st) == 0:
                    st.append(s)
                else:
                    if st[-1] == '(':
                        st.pop()
                    else:
                        st.append(s)
        return len(st)