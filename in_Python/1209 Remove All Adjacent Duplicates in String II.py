class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        st = []
        count = []
        for i in s:
            if len(st) != 0 and st[-1] == i:
                if len(count) != 0:
                    dup = count[-1] + 1
                else:
                    dup = 1
                count.append(dup)
                st.append(i)
            else:
                dup = 1
                st.append(i)
                count.append(dup)
            if dup == k:
                while dup != 0:
                    st.pop()
                    count.pop()
                    dup -= 1
        res = ''
        while len(st) != 0:
            res = st.pop() + res
        return res
            