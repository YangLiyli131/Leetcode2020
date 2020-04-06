class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        dict = {}
        for s in list(text):
            if s in ['b','a','l','o','n']:
                if s not in dict:
                    dict[s] = 1
                else:
                    dict[s] += 1
        t = []
        for s in ['b','a','n','o','l']:
            if s not in dict:
                return 0
            else:
                t.append(dict[s])
        a = min(t[0:3])
        b = min(t[3:])
        if b > a*2:
            return a
        else:
            return b/2