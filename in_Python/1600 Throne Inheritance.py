class ThroneInheritance(object):

    def __init__(self, kingName):
        """
        :type kingName: str
        """
        self.res = [kingName]
        self.relation = {}
        self.dead = set()
        

    def birth(self, parentName, childName):
        """
        :type parentName: str
        :type childName: str
        :rtype: None
        """
        if parentName not in self.relation:
            self.relation[parentName] = [childName]
        else:
            self.relation[parentName].append(childName)

    def death(self, name):
        """
        :type name: str
        :rtype: None
        """
        self.dead.add(name)

    def getInheritanceOrder(self):
        """
        :rtype: List[str]
        """
        res = []
        q = [self.res[0]]
        while q:
            h = q.pop()
            if h not in self.dead:
                res.append(h)
            if h in self.relation:
                nex = self.relation[h]
                nex = nex[::-1]
                q += nex
        return res
        
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()