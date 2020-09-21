class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        n = len(groupSizes)
        dict = {}
        for gi in range(n):
            key = groupSizes[gi]
            if key not in dict:
                temp = []
                temp.append(gi)
                dict[key] = temp
            else:
                temp = dict[key]
                temp.append(gi)
                dict[key] = temp
        res = []
        for key in dict:
            members = dict[key]
            num = len(dict[key]) / key
            while num != 0:
                temp = []
                num -= 1
                for j in range(key):
                    temp.append(members.pop())
                res.append(temp)
        return res
                
                