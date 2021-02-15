class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        i,j = king[0], king[1]
        r = []
        q = set()
        for x in queens:
            q.add(tuple(x))
        while i >= 0:
            if (i,king[1]) in q:
                r.append([i,king[1]])
                break
            i -= 1
        i = king[0]
        while i < 8:
            if (i,king[1]) in q:
                r.append([i,king[1]])
                break
            i += 1
        while j < 8:
            if (king[0],j) in q:
                r.append([king[0],j])
                break
            j += 1
        j = king[1]
        while j >= 0:
            if (king[0],j) in q:
                r.append([king[0],j])
                break
            j -= 1
        i,j = king[0], king[1]
        while i >= 0 and j >= 0:
            if (i,j) in q:
                r.append([i,j])
                break
            i -= 1
            j -= 1
        i,j = king[0], king[1]
        while i < 8 and j < 8:
            if (i,j) in q:
                r.append([i,j])
                break
            i += 1
            j += 1
        i,j = king[0], king[1]
        while i >= 0 and j < 8:
            if (i,j) in q:
                r.append([i,j])
                break
            i -= 1
            j += 1
        i,j = king[0], king[1]
        while i < 8 and j >= 0:
            if (i,j) in q:
                r.append([i,j])
                break
            i += 1
            j -= 1
        return r