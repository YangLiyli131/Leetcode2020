class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.b = [homepage]
        self.f = []

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.b.append(url)
        self.f = []

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while (steps and len(self.b) != 1):
            self.f.append(self.b.pop())
            steps -= 1
        return self.b[-1]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while (steps and len(self.f) != 0):
            self.b.append(self.f.pop())
            steps -= 1
        return self.b[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)