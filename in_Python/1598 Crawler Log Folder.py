class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        st = []
        for x in logs:
            if x != "./" and x != '../':
                st.append(x)
            elif x == '../':
                if len(st) != 0:
                    st.pop()
        return len(st)