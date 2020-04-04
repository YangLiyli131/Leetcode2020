class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        st = []
        for i in ops:
            if i not in ['C','+','D']:
                st.append(int(i))
            elif i == 'C':
                st.pop()
            elif i == 'D':
                st.append(st[-1] * 2)
            else:
                st.append(st[-1] + st[-2])
        return sum(st)
        