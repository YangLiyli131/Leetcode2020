class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        res = []
        d = {}
        for i in range(len(ppid)):
            cur = ppid[i]
            ch = pid[i]
            if cur not in d:
                d[cur] = [ch]
            else:
                d[cur].append(ch)
        if kill not in d:
            return [kill]
        q = collections.deque()
        q.append(kill)
        while q:
            n = len(q)
            while n != 0:
                n -= 1
                h = q.popleft()
                res.append(h)
                if h in d:
                    for nex in d[h]:
                        q.append(nex)
        return res