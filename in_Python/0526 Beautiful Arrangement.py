class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = []
        for num in range(1, n+1):
            if num % 1 == 0 or 1 % num == 0:
                total.append([num])
        for i in range(2, n+1):
            tmp = []
            for x in total:
                for value in range(1, n+1):
                    if value in x:
                        continue
                    if value % i == 0 or i % value == 0:
                        now = x[:]
                        now.append(value)
                        tmp.append(now)
            total = tmp
        return len(total)