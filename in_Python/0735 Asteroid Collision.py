class Solution(object):
    def collide(self, a, b):
        if a > 0 and b < 0:
            return True
        return False
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        st = []
        st.append(asteroids[0])
        for i in range(1, len(asteroids)):
            num = asteroids[i]
            if len(st) == 0:
                st.append(num)
                continue
            if not self.collide(st[-1], num):
                st.append(num)
            else:
                while num != 0 and len(st) != 0 and self.collide(st[-1], num):
                    p = st.pop()
                    if abs(p) > abs(num):
                        num = p
                    elif abs(p) == abs(num):
                        num = 0
                if num != 0:
                    st.append(num)
        return st