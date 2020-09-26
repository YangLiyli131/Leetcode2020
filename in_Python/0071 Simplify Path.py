class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        s = []
        paths = path.split('/')
        print(paths)
        actualpaths = []
        for p in paths:
            if p == '':
                continue
            elif p == '.':
                continue
            elif p == '..':
                if len(actualpaths) != 0:
                    actualpaths.pop()
            else:
                actualpaths.append(p)
        res = '/'
        for i in actualpaths:
            res = res + i + '/'
        if len(res) <= 1:
            return res
        return res[0 : -1]