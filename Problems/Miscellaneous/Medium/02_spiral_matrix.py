# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        answer = list()
        height = len(matrix)
        width = len(matrix[0])
        total_nums = height * width
        turns = 0
        numbers_visited = 0
        row, col = 0, 0
        while numbers_visited < total_nums:
            modulo = turns % 4
            if modulo == 0:
                for i in range(width):
                    answer.append(matrix[row][col + i])
                numbers_visited += width
                col += width - 1
            elif modulo == 1:
                for i in range(1, height - 1):
                    answer.append(matrix[row + i][col])
                numbers_visited += height - 2
                row += height - 1
            elif modulo == 2:
                for i in range(width):
                    answer.append(matrix[row][col - i])
                numbers_visited += width
                col -= width - 1
                width -= 2
            else:
                for i in range(1, height - 1):
                    answer.append(matrix[row - i][col])
                numbers_visited += height - 2
                row -= height - 2
                height -= 2
                col += 1
            turns += 1
        return answer
