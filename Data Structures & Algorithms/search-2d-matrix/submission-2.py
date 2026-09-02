class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix)-1

        while top <= bottom:
            nearby_middle = top+(bottom-top)//2

            if matrix[nearby_middle][0] == target:
                return True
            if matrix[nearby_middle][len(matrix[nearby_middle])-1] == target:
                return True
            elif matrix[nearby_middle][0] < target and matrix[nearby_middle][len(matrix[nearby_middle])-1]<target:
                top = nearby_middle + 1
            elif matrix[nearby_middle][0] < target and matrix[nearby_middle][len(matrix[nearby_middle])-1]>target:
                left = 0
                right = len(matrix[nearby_middle])-1
                while left <= right:
                    mid = left + (right-left)//2
                    if matrix[nearby_middle][mid] == target:
                        return True
                    elif matrix[nearby_middle][mid] < target:
                        left = mid + 1
                    else:
                        right = mid -1
                return False
            else:
                bottom = nearby_middle-1
        return False