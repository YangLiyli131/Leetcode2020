class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        res = ''
        rescount = 0
        for w in words:
            L = len(w)
            eligible = True
            for i in range(1,L+1):
                ss = w[0 : i]
                if ss not in words:
                    eligible = False
                    break
            if eligible:
                if res == '':
                    res = w
                    rescount = len(w)
                else:
                    if rescount < len(w):
                        res = w
                        rescount = len(w)
                    elif rescount == len(w):
                        if w < res:
                            res = w
        return res