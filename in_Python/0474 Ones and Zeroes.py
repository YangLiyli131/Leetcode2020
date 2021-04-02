class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        w = {}
        seen = {}
        def dp(a,b,arr,i):
            if (a,b,i) in seen:
                return seen[(a,b,i)]
            if len(arr) == i:
                return 0
            cur = arr[i]
            if cur in w:
                nz = w[cur][0]
                no = w[cur][1]
            else:
                cc = collections.Counter(cur)
                nz,no = cc['0'], cc['1']
                w[cur] = [cc['0'],cc['1']]
            if nz > a or no > b:
                rs = dp(a, b, arr, i+1)
                seen[(a,b,i)] = rs
                return rs
            rs = max(1 + dp(a-nz, b-no, arr, i+1), dp(a, b, arr, i+1))
            if (a,b,i) not in seen:
                seen[(a,b,i)] = rs
            return rs
        return dp(m,n,strs,0)