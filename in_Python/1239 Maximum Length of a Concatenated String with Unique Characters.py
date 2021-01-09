class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        res = 0
        bt = []
        
        tmp = []
        for x in arr:
            ss = set()
            f = 0
            for xi in x:
                if xi in ss:
                    f = 1
                    break
                ss.add(xi)
            if f == 0:
                tmp.append(x)
        arr = tmp[:]
        
        for i in range(len(arr)):
            bt.append([i])
            res = max(res, len(arr[i]))
        
        def helper(arr,pre):
            r = 0
            for i in range(len(arr)):
                if i in pre:
                    r += len(arr[i])
            return r
        def check(arr, L, w):
            for x in L:
                for wi in w:
                    if wi in arr[x]:
                        return False
            return True
            
        added = True
        while added:
            added = False
            cur = []
            for pre in bt:             
                for i in range(max(pre),len(arr)):
                    neeword = arr[i]
                    if check(arr, pre, neeword):
                        added = True
                        tmp = pre[:]
                        tmp.append(i)
                        cur.append(tmp)
                        res = max(res, len(neeword) + helper(arr,pre))
            bt = cur            
        return res
