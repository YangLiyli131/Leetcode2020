class Solution(object):
    def ambiguousCoordinates(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        S = s[1:-1]
        def f(s):
            if not s or len(s) > 1 and s[0] == s[-1] == '0':
                return []
            if s[-1] == '0':
                return [s]
            if s[0] == '0':
                return [s[0] + '.' + s[1:]]
            return [s] + [s[:i] + '.' + s[i:] for i in range(1, len(s))]
        return ['(%s, %s)' % (a, b) for i in range(len(S)) for a, b in itertools.product(f(S[:i]), f(S[i:]))]