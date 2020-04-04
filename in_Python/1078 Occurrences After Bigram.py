class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        t = text.split(" ")
        res = []
        if len(t) < 4: return res
        for i in range(len(t)-2):
            if t[i] == first and t[i+1] == second:
                res.append(t[i+2])
                i += 2
        return res
        