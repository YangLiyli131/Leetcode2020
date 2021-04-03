class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        letter = coordinates[0]
        idx = int(coordinates[1])
        if letter in 'aceg':
            if idx % 2 == 1:
                return False
            else:
                return True
        else:
            if idx % 2 == 1:
                return True
            else:
                return False
        return True