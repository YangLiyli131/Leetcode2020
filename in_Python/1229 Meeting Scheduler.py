class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        res = []
        i,j = 0,0
        
        slots1 = sorted(slots1, key = lambda x : x[0])
        slots2 = sorted(slots2, key = lambda x : x[0])
        
        def overlap(a,b):
            return a[0] <= b[1] and b[0] <= a[1]
        def lap(a,b):
            return [max(a[0],b[0]), min(a[1],b[1])]
        
        while i < len(slots1) and j < len(slots2):
            a = slots1[i]
            b = slots2[j]
            if overlap(a,b):
                tmp = lap(a,b)
                if tmp[1] - tmp[0] >= duration:
                    return[tmp[0], tmp[0] + duration]
                else:
                    if a[1] > b[1]:
                        j += 1
                    else:
                        i += 1
            else:
                if a[0] > b[1]:
                    j += 1
                elif a[1] < b[0]:
                    i += 1
        return res