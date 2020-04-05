class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left,right+1):
            n = i
            flag = True
            while i != 0:
                cur = i % 10
                if cur == 0:
                    flag = False
                    break
                else:
                    if n % cur != 0:
                        flag = False
                        break
                i /= 10
            if flag:
                res.append(n)
        return res
        