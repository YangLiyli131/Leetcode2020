class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ans = [0] * n
        st = []
        for xs in logs:
            x = xs.split(':')
            idx = int(x[0])
            act = x[1]
            time = int(x[2])
            if act == 'start':
                if len(st) != 0:
                    ans[st[-1][0]] += time - st[-1][1] 
                st.append([idx, time])
            else:
                prev = st.pop()
                ans[idx] += time - prev[1] + 1
                if len(st) != 0:
                    st[-1] = [st[-1][0], time+1]
        return ans