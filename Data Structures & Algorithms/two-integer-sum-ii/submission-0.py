class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size_of_nums = len(numbers)
        for index in range(1, size_of_nums):
            if numbers[index-1] + numbers[index] == target:
                return [index, index+1]
                