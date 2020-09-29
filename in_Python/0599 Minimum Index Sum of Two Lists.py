class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {}
        dd = {}
        for i in range(len(list1)):
            r = list1[i]
            d[r] = i
        for i in range(len(list2)):
            r = list2[i]
            dd[r] = i
        minid = len(list1) + len(list2)
        res = []
        for k in d:         
            if k in dd:
                cursum = dd[k] + d[k]
                if cursum < minid:
                    res = []
                    minid = cursum
                    res.append(k)
                elif cursum == minid:
                    res.append(k)                   
        return res