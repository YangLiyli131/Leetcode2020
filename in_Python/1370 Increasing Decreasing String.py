class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        backbone = []
        dict = {}
        for ss in s:
            if ss not in backbone:
                backbone.append(ss)
            if ss not in dict:
                dict[ss] = 1
            else:
                dict[ss] = dict[ss] + 1
        backbone.sort()
        backbone_rev = []
        for b in backbone:
            backbone_rev.insert(0, b)
        order = 1
        while dict:
            if order == 1:
                template = backbone
                order = 2
            else:
                template = backbone_rev   
                order = 1
            for b in template:
                if b in dict:
                    res.append(b)
                    dict[b] = dict[b] - 1
                    if dict[b] == 0:
                        del dict[b]
        result = ""
        for i in res:
            result += i
        return result