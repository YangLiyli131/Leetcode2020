class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        if number not in self.d:
            self.d[number] = 1
        else:
            self.d[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for k in self.d:
            if value - k in self.d:
                if value - k == k and self.d[k] == 1:
                    continue
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)