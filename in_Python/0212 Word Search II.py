class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = {}
        for w in words:
            t = trie
            for c in w:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = '#'
        self.res = set()
        self.used = []
        for i in range(len(board)):
            self.used.append([False] * len(board[0]))
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, trie, '')
        return list(self.res)
    
    def dfs(self, board, i, j, trie, s):
        if '#' in trie:
            self.res.add(s)
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return 
        if not self.used[i][j] and board[i][j] in trie:
            self.used[i][j] = True
            self.dfs(board, i+1, j, trie[board[i][j]], s + board[i][j])
            self.dfs(board, i-1, j, trie[board[i][j]], s + board[i][j])
            self.dfs(board, i, j+1, trie[board[i][j]], s + board[i][j])
            self.dfs(board, i, j-1, trie[board[i][j]], s + board[i][j])
            self.used[i][j] = False



class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        prefix = set()
        for w in words:
            for i in range(1, len(w)+1):
                prefix.add(w[:i])
        base = set(words)
        res = set()
        row = len(board)
        col = len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for i in range(row):
            for j in range(col):
                cur = board[i][j]
                q = collections.deque()
                q.append([i,j,cur,{(i,j)}])
                while q:
                    thisi, thisj, prestr, path = q.popleft()
                    if prestr not in prefix:
                        continue
                    if prestr in base:
                        res.add(prestr)
                    if prestr[::-1] in base:
                        res.add(prestr[::-1])
                    for d in directions:
                        nexti,nextj = thisi + d[0], thisj + d[1]
                        if 0 <= nexti < row and 0 <= nextj < col and (nexti, nextj) not in path:
                            q.append([nexti, nextj, prestr + board[nexti][nextj], path.union({(nexti,nextj)})])
        return list(res)