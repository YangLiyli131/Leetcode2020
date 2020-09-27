class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """     
        ccc = 'abcdefghijklmnopqrstuvwxyz'
        res = ''
        for i in range(len(s)):
            if s[i] != '?':
                res += s[i]
            else:
                if i+1 < len(s) and s[i+1] == '?':
                    if i == 0:
                        res += 'a'
                    else:
                        for ch in ccc:
                            if ch != s[i-1] and ch != res[i-1]:
                                res += ch
                                break
                if i+1 < len(s) and s[i+1] != '?':   
                    if i == 0:
                        for ch in ccc:
                            if ch != s[i+1] :
                                res += ch
                                break
                    else:
                        for ch in ccc:
                            if ch != s[i-1] and ch != s[i+1] and ch != res[i-1]:
                                res += ch
                                break
                if i+1 == len(s):
                    if i == 0:
                        res += 'a'
                    else:
                        for ch in ccc:
                                if ch != s[i-1] and ch != res[i-1]:
                                    res += ch
                                    break
        return res
                    
        