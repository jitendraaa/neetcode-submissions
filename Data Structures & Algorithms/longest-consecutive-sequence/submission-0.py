class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        max_size = 0
        for number in hash_set:
            if number-1 not in hash_set:
                current_size = 1
                max_size = max(max_size, current_size)
                number = number + 1
                while (number in hash_set):
                    current_size = current_size + 1
                    max_size = max(max_size, current_size)
                    number = number + 1
        return max_size