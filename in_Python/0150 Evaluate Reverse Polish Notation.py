class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st = []
        sy = ['+','-','*','/']
        for t in tokens:
            if t not in sy:
                st.append(int(t))
            else:
                a = int(st.pop())
                b = int(st.pop())
                if t == '+':
                    st.append(a + b)
                elif t == '-':
                    st.append(b - a)
                elif t == '*':
                    st.append(a * b)
                else:
                    if a * b < 0 and b % a != 0:
                        st.append(b/a+1)
                    else:
                        st.append(b/a)
        return st[-1]