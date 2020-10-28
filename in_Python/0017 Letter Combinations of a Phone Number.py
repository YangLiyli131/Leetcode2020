class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        maps = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}
        res = ['']
        if len(digits) == 0:
            return []
        for d in digits:
            cur = []
            for ad in maps[d]:
                for r in res:
                    cur.append(r + ad)
            res = cur
        return res
                
        