class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        q = collections.deque([start])
        seen = {start}
        while q:
            cur = q.popleft()
            if arr[cur] == 0:
                return True
            for nex in [cur-arr[cur], cur+arr[cur]]:
                if 0 <= nex < len(arr) and nex not in seen:
                    q.append(nex)
                    seen.add(nex)
        return False
        
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        adj = {}
        for i in range(len(arr)):
            cur = arr[i]
            left = i - cur
            right = i + cur
            tmp = []
            if left >= 0:
                tmp.append(left)
            if right < len(arr):
                tmp.append(right)
            adj[i] = tmp
        q = [start]
        visited = set()
        while q:
            n = len(q)
            while n != 0:
                n -= 1
                h = q.pop(0)
                visited.add(h)
                if arr[h] == 0:
                    return True
                for nex in adj[h]:
                    if nex not in visited:
                        q.append(nex)
        return False