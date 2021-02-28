class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        r = 0
        idx = 0
        if ruleKey == 'color':
            idx = 1
        elif ruleKey == 'name':
            idx = 2
        for x in items:
            if x[idx] == ruleValue:
                r += 1
        return r