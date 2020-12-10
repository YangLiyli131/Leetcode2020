class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        res = []
        level = math.floor(math.log(label, 2)) 
        while level != 0:
            res.insert(0, label)
            upper = label / 2
            dis = math.pow(2, level) - 1 - upper
            level -= 1
            label = int(math.pow(2, level) + dis)
        res.insert(0, 1)
        return res
            