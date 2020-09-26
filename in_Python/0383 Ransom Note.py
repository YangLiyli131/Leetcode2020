class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dm = {}
        for m in magazine:
            if m not in dm:
                dm[m] = 1
            else:
                dm[m] += 1
        dr = {}
        for m in ransomNote:
            if m not in dr:
                dr[m] = 1
            else:
                dr[m] += 1
        for k in dr:
            if k not in dm:
                return False
            if dr[k] > dm[k]:
                return False
        return True