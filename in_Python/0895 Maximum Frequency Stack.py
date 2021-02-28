class FreqStack(object):

    def __init__(self):
        self.st = []
        self.d = {}
        self.v = {}
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.st.append(x)
        if x not in self.d:
            self.d[x] = 1
            if 1 in self.v:
                self.v[1].append(x)
            else:
                self.v[1] = [x]
        else:
            self.v[self.d[x]].remove(x)
            self.d[x] += 1
            v = self.d[x]
            if v not in self.v:
                self.v[v] = [x]
            else:
                self.v[v].append(x)
                
    def pop(self):
        """
        :rtype: int
        """
        mx = max(self.v.keys())
        ca = self.v[mx]
        t = []
        while self.st and self.st[-1] not in ca:
            t.append(self.st.pop())
        p = self.st.pop()
        while t:
            self.st.append(t.pop())
        vp = self.d[p]
        self.d[p] = vp-1
        self.v[vp].remove(p)
        if len(self.v[vp]) == 0:
            self.v.pop(vp,'None')
        if vp-1 not in self.v:
            self.v[vp-1] = [p]
        else:
            self.v[vp-1].append(p)
        return p


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()