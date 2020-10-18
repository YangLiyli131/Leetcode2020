class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = []
        self.values = []
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.keys:
            self.keys.append(key)
            self.values.append(value)
        else:
            for i in range(len(self.keys)):
                if self.keys[i] == key:
                    self.values[i] = value
                    break

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        if key not in self.keys:
            return -1
        else:
            for i in range(len(self.keys)):
                if self.keys[i] == key:
                    return self.values[i]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        idx = -1
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                idx = i
                break
        if idx != -1:
            a = []
            b = []
            for i in range(len(self.keys)):
                if i == idx:
                    continue
                a.append(self.keys[i])
                b.append(self.values[i])
            self.keys = a
            self.values = b
                


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)