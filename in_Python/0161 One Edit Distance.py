class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return self.isOneEditDistance(t,s)
        if abs(len(s) - len(t)) > 1 or s == t:
            return False
        for i in range(len(s)):
            if s[i] != t[i]:
                return s[i+1:] == t[i+1:] or s[i:] == t[i+1:]
        return True

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == None and t == None:
            return False
        if abs(len(s) - len(t)) > 1:
            return False
        if len(s) - len(t) == 1:
            for i in range(len(s)):
                cur = s[:i] + s[i+1:]
                if cur == t:
                    return True
        elif len(t) - len(s) == 1:
            for i in range(len(t)):
                cur = t[:i] + t[i+1:]
                if cur == s:
                    return True
        else:
            if t == s:
                return False
            backs = set()
            for i in range(len(s)):
                cur = s[:i] + '*' + s[i+1:]
                backs.add(cur)
            for i in range(len(t)):
                cur = t[:i] + '*' + t[i+1:]
                if cur in backs:
                    return True
        return False