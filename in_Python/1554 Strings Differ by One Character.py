class Solution(object):
    def differByOne(self, dict):
        """
        :type dict: List[str]
        :rtype: bool
        """
        d = set()
        for x in dict:
            for i in range(len(x)):
                ns = x[:i] + '*' + x[i+1:]
                if ns in d:
                    return True
                d.add(ns)
        return False
        