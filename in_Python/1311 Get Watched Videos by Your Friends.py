class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        q = collections.deque()
        q.append(id)
        l = -1
        people = []
        seen = set()
        seen.add(id)
        while q:
            n = len(q)
            cur = []
            while n != 0:
                n -= 1
                h = q.popleft()
                for nex in friends[h]:
                    if nex not in seen:
                        seen.add(nex)
                        q.append(nex)
                cur.append(h)
            l += 1
            if l == level:
                people = cur[:]
                break
        d = {}
        for x in people:
            for y in watchedVideos[x]:
                if y not in d:
                    d[y] = 1
                else:
                    d[y] += 1
        count = {}
        for key in d:
            v = d[key]
            if v not in count:
                count[v] = [key]
            else:
                count[v].append(key)
        res = []
        keys = count.keys()
        keys.sort()
        for key in keys:
            v = count[key]
            v.sort()
            for x in v:
                res.append(x)
        return res
                
        