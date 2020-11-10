class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        st = []
        chk = None
        for i in preorder:
            while st and st[-1] < i:
                chk = st.pop()
            if chk and chk > i:
                return False
            st.append(i)
        return True
        