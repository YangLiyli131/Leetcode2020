class Solution(object):
    def maxBoxesInWarehouse(self, boxes, warehouse):
        """
        :type boxes: List[int]
        :type warehouse: List[int]
        :rtype: int
        """
        boxes.sort()
        curmin = [warehouse[0]]
        cm = curmin[0]
        for i in range(1, len(warehouse)):
            cur = warehouse[i]
            if cur < cm:
                cm = cur
            curmin.append(cm)
        i,j = 0, len(warehouse)-1
        r = 0
        while j >= 0 and i < len(boxes):
            if curmin[j] >= boxes[i]:
                i += 1
                r += 1
            j -= 1
        return r