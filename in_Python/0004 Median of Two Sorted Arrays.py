class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        q1 = []
        q2 = []
        heapq.heapify(q1)
        heapq.heapify(q2)
        for n in nums1 + nums2:
            if len(q1) == 0:
                heapq.heappush(q1,-n)
            else:
                maxq1 = -heapq.heappop(q1)
                if n >= maxq1:
                    heapq.heappush(q1,-maxq1)
                    heapq.heappush(q2,n)
                else:
                    heapq.heappush(q1,-n)
                    heapq.heappush(q2,maxq1)
                if len(q2) - len(q1) > 1:
                    heapq.heappush(q1, -heapq.heappop(q2))
        #print(q1)
        #print(q2)
        if len(q1) == len(q2):
            a = -heapq.heappop(q1)
            b = heapq.heappop(q2)
            return (a+b) / float(2)
        if len(q2) == 0:
            return -heapq.heappop(q1)
        return heapq.heappop(q2)
                    
                
        