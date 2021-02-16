class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        for i, x in enumerate(s):
            if x not in d:
                d[x] = i
            else:
                d[x] = max(d[x],i)
        st = []
        for i, c in enumerate(s):
            if c in st:
                continue
            while st and st[-1] > c and i < d[st[-1]]:
                st.pop()
            st.append(c)
        return ''.join(st)