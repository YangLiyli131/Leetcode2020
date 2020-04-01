class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        t = S.split(' ')
        id = 1
        for i in range(len(t)):
            x = t[i]
            if x[0] in ['a','e','i','o','u','A','E','I','O','U']:
                t[i] = x + 'ma'
            else:
                t[i] = x[1:] + x[0] + 'ma'
            t[i] += 'a' * id
            id += 1
        res = ""
        for i in t: res += i + ' '
        return res.strip()
        