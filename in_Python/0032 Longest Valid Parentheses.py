class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        def check(a,b):
            if a[0] <= b[0] and a[1] >= b[1]:
                return 1
            if a[0] >= b[0] and a[1] <= b[1]:
                return 2
            if a[1] == b[0]-1:
                return 3
            if b[1] == a[0]-1:
                return 4
            return 5
        arr = []
        st = []
        for i,x in enumerate(s):
            if x == '(':
                st.append([i,x])
            else:
                if not st:
                    continue
                pre = st.pop()
                if not arr:
                    heapq.heappush(arr, [pre[0], i])
                else:
                    last = arr[-1]
                    arr = arr[:-1]
                    cur = [pre[0], i]
                    t = check(last, cur)
                    if t == 1:
                        heapq.heappush(arr, last)
                    if t == 2:
                        heapq.heappush(arr, cur)
                    if t == 3:
                        heapq.heappush(arr, [last[0], cur[1]])
                    if t == 4:
                        heapq.heappush(arr, [cur[0], last[1]])
                    if t == 5:
                        heapq.heappush(arr, last)
                        heapq.heappush(arr, cur)
        ls = [0] * len(s)
        for x in arr:
            for idx in range(x[0], x[1]+1):
                ls[idx] = 1
        res = 0
        i = 0
        while i < len(s):
            if ls[i] == 0:
                i += 1
                continue
            j = i
            while j < len(s) and ls[j] == 1:
                j += 1
            res = max(res, j - i)
            i = j
        return res
                