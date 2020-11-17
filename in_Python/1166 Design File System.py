class FileSystem(object):

    def __init__(self):
        self.path = {}

    def createPath(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """
        idx = -1
        for i in range(len(path)-1, -1, -1):
            if path[i] == '/':
                idx = i
                break
        if idx == 0:
            if path in self.path:
                return False
            else:
                self.path[path] = value
                return True
        else:
            pre = path[:idx]
            if pre not in self.path:
                return False
            else:
                if path in self.path:
                    return False
                self.path[path] = value
                return True

    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        if path in self.path:
            return self.path[path]
        return -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)