class Solution(object):
    def isD(self, c):
        return '0' <= c <= '9'
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = []
        for ch in s:
            if ch != ']':
                st.append(ch)
            else:
                newstr = []
                while st and st[-1] != '[':
                    newstr.insert(0, st.pop())
                st.pop()
                nst = ''.join(newstr)
                count = []
                while st and self.isD(st[-1]):
                    count.insert(0,st.pop())
                count = int(''.join(count))
                while count != 0:
                    count -= 1
                    st.append(nst)
        return ''.join(st)