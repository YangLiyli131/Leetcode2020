class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        s = []
        for i in range(len(paths)):
            s.append(paths[i][0])
        for i in range(len(paths)):
            if paths[i][1] not in s:
                res = paths[i][1]
                break
        return res