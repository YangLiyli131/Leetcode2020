class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word
        idxx = 0
        for idx, l in enumerate(word):
            if l == ch:
                idxx = idx
                break
        pre, nex = word[:idxx+1], word[idxx+1:]
        return pre[::-1] + nex