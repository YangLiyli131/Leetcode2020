class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        d = {}
        for idx, letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
            d[letter] = idx
        res = len(word)
        for i in range(len(word)):
            cur = word[i]
            if i == 0:
                pre = 'a'
            else:
                pre = word[i-1]
            dis = abs(d[cur] - d[pre])
            res += min(dis, 26 - dis)
        return res