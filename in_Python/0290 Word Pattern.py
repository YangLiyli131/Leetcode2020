class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        if pattern == None and s == None:
            return True
        if pattern == None or s == None:
            return False
        p = s.split(' ')
        if len(pattern) != len(p):
            return False
        dict = {}
        for i in range(len(p)):
            k = pattern[i]
            v = p[i]
            if k in dict and dict[k] != v:
                return False
            for key in dict:
                if dict[key] == v and key != k:
                    return False
            if k not in dict:
                dict[k] = v
        return True
            
                
        