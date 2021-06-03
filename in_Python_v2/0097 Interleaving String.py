class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l:
            return False
        q = collections.deque()
        v = set()
        q.append((0,0))
        v.add((0,0))
        while q:
            x, y = q.popleft()
            if x + y == l:
                return True
            if x+1 <= r and s1[x] == s3[x+y] and (x+1,y) not in v:
                q.append((x+1,y))
                v.add((x+1,y))
            if y+1 <= c and s2[y] == s3[x+y] and (x,y+1) not in v:
                q.append((x,y+1))
                v.add((x,y+1))
        return False