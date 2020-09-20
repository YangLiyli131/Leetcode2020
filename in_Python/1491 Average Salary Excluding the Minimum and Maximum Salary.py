class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        smax = salary[0]
        smin = salary[0]
        ssum = 0
        for sa in salary:
            ssum += sa
            if sa > smax:
                smax = sa
            if sa < smin:
                smin = sa
        return (ssum - smax - smin) / float((len(salary)-2))
        