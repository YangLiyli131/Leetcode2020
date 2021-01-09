class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        res = []
        seen = set()
        base = set(wordList)
        q = collections.deque()
        q.append([beginWord,1, [beginWord]])
        while q:
            qq = collections.deque()
            newkeys = set()
            while q:
                word, count, L = q.popleft()
                if word == endWord:
                    if len(res) == 0 or len(L) == len(res[0]):
                        res.append(L)
                        continue
                    if len(L) < len(res[0]):
                        res = []
                        res.append(L)
                        continue
                for i in range(len(word)):
                    for j in range(26):
                        newword = word[:i] + chr(ord('a')+j) + word[i+1:]
                        if newword == word:
                            continue
                        if newword in base and newword not in L:
                            qq.append([newword, count+1, L + [newword]])
                            newkeys.add(newword)
            base -= newkeys
            q = qq
        return res