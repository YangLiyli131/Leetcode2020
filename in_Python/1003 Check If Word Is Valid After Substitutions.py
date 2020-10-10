class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        for x in s:
            if x == 'a' or x == 'b':
                st.append(x)
            else:
                if len(st) < 2: 
                    st.append(x)
                else:
                    if st[-1] == 'b' and st[-2] == 'a':
                        st.pop()
                        st.pop()
        return len(st) == 0
        