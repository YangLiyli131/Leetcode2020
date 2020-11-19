class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        adj_list = {}
        for e in edges:
            source = e[0]
            target = e[1]
            if source not in adj_list:
                adj_list[source] = [target]
            else:
                adj_list[source].append(target)
            if target not in adj_list:
                adj_list[target] = [source]
            else:
                adj_list[target].append(source)
        for i in range(n):
            if i not in adj_list:
                adj_list[i] = []
        ans = [0] * n
        seen = set()
        
        def dfs(node):
            counter = collections.Counter()
            if node not in seen:
                counter[labels[node]] += 1
                seen.add(node)
                for x in adj_list[node]:
                    counter += dfs(x)
                ans[node] = counter[labels[node]]
            return counter
        
        dfs(0)
        return ans