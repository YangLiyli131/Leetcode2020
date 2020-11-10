class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.arr = [{}]

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.arr[-1][index] = val

    def snap(self):
        """
        :rtype: int
        """
        self.arr.append({})
        return len(self.arr)-2

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        while snap_id >= 0:
            if index in self.arr[snap_id]:
                return self.arr[snap_id][index]
            snap_id -= 1
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)