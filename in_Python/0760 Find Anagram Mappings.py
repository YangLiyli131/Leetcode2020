class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        arr = [0] * len(A)
        d = {}
        for i in range(len(B)):
            letter = B[i]
            if letter not in d:
                d[letter] = [i]
            else:
                d[letter].append(i)
        for i in range(len(A)):
            cur = A[i]
            row = d[cur]
            x = row.pop()
            arr[i] = x
            d[cur] = row
        return arr