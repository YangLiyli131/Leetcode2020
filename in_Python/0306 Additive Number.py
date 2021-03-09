class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) < 3:
            return False
        base = []
        def h(s):
            res = 0
            for i in range(len(s)):
                res = res * 10 + int(s[i])
            return res
        for i in range(1,len(num)):
            pre = num[:i]
            for j in range(i+1, len(num)):
                sec = num[i:j]
                nex = num[j:]
                if len(pre) > 1 and pre[0] == '0':
                    continue
                if len(sec) > 1 and sec[0] == '0':
                    continue
                base.append([h(pre),h(sec),nex])
        change = 1
        while change:
            change = 0
            newbase = []
            for x in base:
                a,b,c = x[-3],x[-2],x[-1]
                tmp = a+b
                if c == str(tmp):
                    return True
                if c.startswith(str(tmp)):
                    change = 1
                    newc = c[len(str(tmp)):]
                    cur = x[:-1]
                    cur.append(tmp)
                    cur.append(newc)
                    newbase.append(cur)
            base = newbase
        return False
                