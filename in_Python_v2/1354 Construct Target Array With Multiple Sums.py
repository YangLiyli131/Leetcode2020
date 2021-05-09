class Solution(object):
    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        if len(target) == 1:
            return target == [1]
        s = sum(target)
        hq = [-x for x in target]
        heapq.heapify(hq)
        while -hq[0] > 1:
            first = -hq[0]
            restsum = s - first
            if restsum == 1:
                return True
            newfirst = first % restsum
            if newfirst == 0 or newfirst == first:
                return False
            heapq.heapreplace(hq, -newfirst)
            s -= first - newfirst
        return True
            
        