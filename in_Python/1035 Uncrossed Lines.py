class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        memo = {}
        def helper(a,b):
            if a >= len(A) or b >= len(B):
                return 0
            if (a,b) in memo:
                return memo[(a,b)]
            if A[a] == B[b]:
                ans = helper(a+1,b+1) + 1
            else:
                ans = max(helper(a+1,b), helper(a,b+1))
            memo[(a,b)] = ans
            return ans
        
        return helper(0,0)