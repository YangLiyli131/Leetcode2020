class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        def check(x):
            return '0' <= x <= '9'
        L = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and check(s[j]):
                j += 1
            L.append(s[i:j])
            while j < len(s) and s[j] == ' ':
                j += 1
            if j < len(s):
                L.append(s[j])
            i = j + 1
            while i < len(s) and s[i] == ' ':
                i += 1
        st = []
        i = 0
        #print(L)
        while i < len(L):
            x = L[i]
            if x not in ['/','*']:
                st.append(x)
                i += 1
            else:
                pre = int(st.pop())
                nex = int(L[i+1])
                if x == '/':
                    st.append(str(pre / nex))
                else:
                    st.append(str(pre * nex))
                i += 2
        #print(st)
        res = int(st[0])
        i = 1
        while i < len(st):
            if st[i] == '+':
                res += int(st[i+1])
            else:
                res -= int(st[i+1])
            i += 2
        return res
                
        