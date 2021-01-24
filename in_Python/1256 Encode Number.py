class Solution(object):
    def encode(self, num):
        """
        :type num: int
        :rtype: str
        """
        st = []
        n = num + 1
        while n != 0:
            c = n % 2
            st.append(str(c))
            n /= 2
        st = st[::-1]
        return ''.join(st[1:])