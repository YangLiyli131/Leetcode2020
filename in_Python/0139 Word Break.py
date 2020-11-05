class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if wordDict == None or len(wordDict) == 0:
            return False
        base = set(wordDict)
        lengths = set()
        miniL = len(wordDict[0])
        for x in base:
            if len(x) < miniL:
                miniL = len(x)
            lengths.add(len(x))
        dp = [0] * len(s)
        dp.insert(0,1)
        i = miniL - 1
        while i < len(s):
            for xl in lengths:
                begin = i + 1 - xl
                if begin >= 0:
                    if dp[begin] == 1 and s[begin : i+1] in base:
                        dp[i+1] = 1
            i += 1
        return dp[-1] == 1