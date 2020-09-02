class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        res = 0
        if 0 not in A and 1 not in A and 2 not in A:
            return ""
        cur = 0
        flag = False
        for i in range(len(A)):
            x1 = A[i] * 1000
            t1 = list(A)
            del t1[i]
            for ii in range(len(t1)):
                x2 = t1[ii] * 100
                t2 = list(t1)
                del t2[ii]
                for iii in range(len(t2)):
                    x3 = t2[iii] * 10
                    t3 = list(t2)
                    del t3[iii]
                    for iiii in t3:
                        x4 = iiii
                        cur = x1 + x2 + x3 + x4
                        if cur >= res and cur < 2359 and cur % 100 < 60:
                            flag = True
                            res = cur
        if flag == False:
            return ""
        if flag and res == 0:
            return '00:00'
        else:
            #print(res)
            rest = ""
            while res != 0:
                rest = str(res%10) + rest
                if len(rest) == 2:
                    rest = ":" + rest
                res /= 10
            while len(rest) != 5:
                rest = '0' + rest
            return rest
            
        