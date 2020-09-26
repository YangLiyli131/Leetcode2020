class MyHashSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.st = {}
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.st[key] = 1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.st.pop(key,1)
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.st
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)