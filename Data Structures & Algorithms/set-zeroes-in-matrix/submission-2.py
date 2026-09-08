class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        apex = matrix[0][0]
        apex_row = 1
        apex_column = 1
        if apex == 0:
            apex_row = 0
            apex_column = 0
        row_size = len(matrix[0])
        column_size = len(matrix)
        for column in range(0, column_size):
            for row in range(0, row_size):
                if matrix[column][row] == 0:
                    if row == 0:
                        apex_row = 0
                    elif column == 0:
                        apex_column = 0
                    else:
                        matrix[0][row] = 0
                        matrix[column][0] = 0
        for column in range(1, column_size):
            for row in range(1, row_size):
                if matrix[0][row] == 0 or matrix[column][0] == 0:
                    matrix[column][row] = 0
        if apex_column == 0:
            for row in range(0, row_size):
                matrix[0][row] = 0
        if apex_row ==0:
            for column in range(0, column_size):
                matrix[column][0] = 0
        return None