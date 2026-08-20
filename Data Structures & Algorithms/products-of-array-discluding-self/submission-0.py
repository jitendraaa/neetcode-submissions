class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size_of_nums = len(nums)
        output = [1]*size_of_nums
        for index in range(1, size_of_nums):
            output[index] = output[index-1] * nums[index-1]

        right_product = 1
        for index in range(size_of_nums-2, -1, -1):
            right_product = right_product * nums[index+1]
            output[index] = output[index] * right_product
        return output