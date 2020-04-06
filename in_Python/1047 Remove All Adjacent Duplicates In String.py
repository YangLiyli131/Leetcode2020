class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        st = []
        for i in list(S):
            if len(st) != 0 and st[-1] == i:
                st.pop()
            else:
                st.append(i)           
        res = ""
        for i in st: res += i
        return res
        