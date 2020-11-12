class Solution(object):
    def di(self,x,y):
        return (x[0]-y[0])*(x[0]-y[0]) + (x[1]-y[1])*(x[1]-y[1])
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        p = [p1,p2,p3,p4]
        d = {}
        for i in range(4):
            a = p[i]
            for j in range(i+1,4):
                b = p[j]
                if a == b:
                    continue
                dis = self.di(a,b)
                if dis in d:
                    d[dis] += 1
                else:
                    d[dis] = 1
        v = d.values()
        v.sort()
        if v == [2,4]:
            return True
        return False