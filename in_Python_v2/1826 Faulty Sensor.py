class Solution(object):
    def badSensor(self, sensor1, sensor2):
        """
        :type sensor1: List[int]
        :type sensor2: List[int]
        :rtype: int
        """
        i = 0
        while i < len(sensor1):
            if sensor1[i] != sensor2[i]:
                if i == len(sensor1) - 1:
                    break
                if sensor1[i+1:] == sensor2[i : len(sensor2)-1]:
                    return 2
                else:
                    return 1
            i += 1
        return -1