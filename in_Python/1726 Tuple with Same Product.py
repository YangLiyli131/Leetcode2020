class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def check(x,y):
            if x[0] in y or x[1] in y or y[0] in x or y[1] in x:
                return False
            return True
        res = 0
        d = {}
        n = len(nums)
        for i in range(n):
            a = nums[i]
            for j in range(i+1,n):
                b = nums[j]
                c = a * b
                if c not in d:
                    d[c] = [[a,b]]
                else:
                    d[c].append([a,b])
        for k in d:
            row = d[k]
            nr = len(row)
            if nr == 1:
                continue
            for i in range(nr):
                x = row[i]
                for j in range(i+1, nr):
                    y = row[j]
                    if check(x,y):
                        res += 1
        return 8 * res