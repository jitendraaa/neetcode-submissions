class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            element = target - num

            if element in hashmap:
                return [hashmap[element], i]
            hashmap[num] = i