class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        i,j = 0,0
        s = []
        for i in range(len(pushed)):
            s.append(pushed[i])
            while len(s) != 0 and s[-1] == popped[j]:
                s.pop()
                j += 1
        while len(s) != 0:
            if s.pop() != popped[j]:
                return False
            j += 1
        return True
        