class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = sorted(words, key = len, reverse = True)
        res = len(words[0]) + 1
        def check(a,b):
            l = len(b)
            for x in a:
                if x[len(x)-l : ] == b:
                    return True
            return False
        
        for i in range(1, len(words)):
            w = words[i]
            pre = words[:i]
            if not check(pre, w):
                res += len(w) + 1
        return res