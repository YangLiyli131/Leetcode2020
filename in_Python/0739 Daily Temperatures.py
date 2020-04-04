class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        st = []
        res = []
        for i in range(len(T)): res.append(0)
        for i in range(len(T)):
            while len(st) != 0 and T[i] > T[st[-1]]:
                res[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)
        while len(st) != 0:
            res[st[-1]] = 0
            st.pop()
        return res
        