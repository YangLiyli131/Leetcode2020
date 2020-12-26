class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        while len(sandwiches) != 0:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students.pop(0))
                if sum(students) == 0 and sandwiches[0] == 1:
                    return len(students)
                if sum(students) == len(students) and sandwiches[0] == 0:
                    return len(students)
        return 0