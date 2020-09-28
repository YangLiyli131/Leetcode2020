"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
        #################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        for e in employees:
            if e.id == id:
                row = e
                break
        res = row.importance
        st = row.subordinates
        visited = []
        while len(st) != 0:
            nextem = st.pop(0)
            if nextem not in visited:
                visited.append(nextem)
                for e in employees:
                    if e.id == nextem:
                        t = e
                        break
                res += t.importance
                for x in t.subordinates:
                    st.append(x)
        return res
            
        
        