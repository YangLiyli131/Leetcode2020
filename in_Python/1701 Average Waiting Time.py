class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        N = len(customers)
        total = customers[0][1]
        pre = customers[0][0] + total
        for i in range(1, N):
            start = customers[i][0]
            time = customers[i][1]
            if start > pre:
                total += time
                pre = start + time
            else:
                total += pre + time - start
                pre += time
        return total / float(N)