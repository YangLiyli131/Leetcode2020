class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if name == typed:
            return True
        if len(name) >= len(typed):
            return False
        i,j = 0,0
        a = []
        while j < len(name):
            while j < len(name) and name[j] == name[i]:
                j += 1
            a.append(name[i:j])
            i = j
        i,j = 0,0
        b = []
        while j < len(typed):
            while j < len(typed) and typed[j] == typed[i]:
                j += 1
            b.append(typed[i:j])
            i = j
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if a[i][0] != b[i][0]:
                return False
            if len(a[i]) > len(b[i]):
                return False
        return True