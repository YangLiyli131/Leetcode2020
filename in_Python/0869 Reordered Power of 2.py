class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        arr = list(str(N))
        arr.sort() 
        st = ''.join(arr)
        cur = 1
        if st == '1':
            return True
        for i in range(1,32):
            cur *= 2
            cc = list(str(cur))
            cc.sort()
            cs = ''.join(cc)
            if cs == st:
                return True
        return False