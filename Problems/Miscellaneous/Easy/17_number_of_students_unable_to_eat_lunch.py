# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        number_counts = {0: 0, 1: 0}
        students_without_lunch = len(students)
        for number in students:
            number_counts[number] += 1
        for number in sandwiches:
            if number_counts[number] == 0:
                return students_without_lunch
            else:
                number_counts[number] -= 1
                students_without_lunch -= 1
        return 0
