class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        b = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(len(a)):
            d[a[i]] = b[i]
        st = []
        for si in s:
            if len(st) != 0 and si in d and d[si] == st[-1] :
                st.pop()
            elif len(st) != 0 and st[-1] in d and d[st[-1]] == si :
                st.pop()
            else:
                st.append(si)
        res = ''
        while len(st) != 0:
            res = st.pop() + res
        return res
        