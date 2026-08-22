class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size_of_nums = len(numbers)
        first_index = 0
        summ = numbers[0]
        for index in range(1, size_of_nums):
            summ = summ + numbers[index]
            while(summ >= target and first_index < index):
                if(summ == target):
                    if numbers[first_index] + numbers[index] == target:
                        return [first_index+1, index+1]
                summ = summ - numbers[first_index]
                first_index = first_index + 1
                

