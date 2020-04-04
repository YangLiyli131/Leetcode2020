class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for w in paths:
            t = w.split(" ")
            for i in range(1,len(t)):            
                s = t[i]
                start = s.index('(')
                end = s.index(')')
                content = s[(start+1):end]
                if content not in dict:
                    temp =  []
                    temp.append(t[0] + '/' + s[0:start])
                    dict[content] = temp
                else:
                    dict[content].append(t[0] + '/' + s[0:start])
        res = []
        for x in dict.values():
            if len(x) != 1: res.append(x)
        return res
        