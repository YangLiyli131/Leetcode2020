class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.d = {}
        self.list = []
        self.n = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.d:
            return -1
        else:
            self.list.remove(key)
            self.list.insert(0,key)
            return self.d[key]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.d:
            self.d[key] = value
            self.list.remove(key)
            self.list.insert(0,key)
        else:
            if len(self.d) < self.n:
                self.d[key] = value
                self.list.insert(0,key)
            else:
                k = self.list.pop()
                self.d.pop(k,None)
                self.d[key] = value
                self.list.insert(0,key)
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)