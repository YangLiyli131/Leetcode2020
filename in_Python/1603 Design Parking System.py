class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.b = big
        self.m = medium
        self.s = small
        

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if carType == 1 and self.b != 0:
            self.b -= 1
            return True
        elif carType == 2 and self.m != 0:
            self.m -= 1
            return True
        elif carType == 3 and self.s != 0:
            self.s -= 1
            return True
        else:
            return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)