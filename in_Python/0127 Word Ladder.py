class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        visited = set()
        wordSet = set(wordList)
        q = [(beginWord, 1)]
        while q:
            word, count = q.pop(0)
            if word == endWord:
                return count
            if word in visited:
                continue
            for i in range(len(word)):
                for j in range(26):
                    ch = ord('a') + j
                    newword = word[0:i] + chr(ch) + word[(i+1):]
                    if newword in wordSet:
                        q.append((newword, count+1))
            visited.add(word)
        return 0


class Solution(object):
    def dis(self, w1, w2):
        i,j = 0,0
        res = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                res += 1
                if res > 1:
                    return False
        return True
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        dict = {}
        if endWord not in wordList:
            return 0
        for w in wordList:
            cur = []
            for ww in wordList:
                if ww == w:
                    continue
                if self.dis(ww,w):
                    cur.append(ww)
            dict[w] = cur
        if beginWord not in wordList:
            cur = []
            for w in wordList:
                if self.dis(w, beginWord):
                    cur.append(w)
            dict[beginWord] = cur            
        res = 0
        q = [beginWord]
        visited = []
        while q:
            n = len(q)
            res += 1
            while n != 0:
                n -= 1
                w = q.pop(0)
                visited.append(w)
                for nx in dict[w]:            
                    if nx == endWord:
                        return res+1
                    if nx not in visited:
                        q.append(nx)
                        visited.append(nx)
        return 0
                