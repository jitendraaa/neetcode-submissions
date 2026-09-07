class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = int((n*(n+1))/2)
        current_sum = 0
        for num in nums:
            current_sum += num
        missing = expected_sum - current_sum
        return missing