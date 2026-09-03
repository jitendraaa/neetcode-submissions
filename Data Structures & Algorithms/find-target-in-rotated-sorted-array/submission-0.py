class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def find_minimum_index(nums):
            left = 0
            size = len(nums)
            right = size-1
            if size == 1:
                return 0
            while left <= right:
                mid = left+(right-left)//2
                if(mid == 0 and nums[mid]<nums[mid+1] and nums[mid]<nums[size-1]):
                    return mid
                elif(mid==size-1 and nums[mid]<nums[mid-1] and nums[mid]<nums[0]):
                    return mid
                elif(nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]):
                    return mid
                elif(nums[mid]>nums[right]):
                    left = mid + 1
                else:
                    right = mid - 1
        def binary_search(nums, left, right, target):
            while left <= right:
                mid = left+(right-left)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        min_index = find_minimum_index(nums)
        if(min_index == 0):
            return binary_search(nums, 0, len(nums)-1, target)
        else:
            left_window = binary_search(nums, 0, min_index-1, target)
            right_window = binary_search(nums, min_index, len(nums)-1, target)
            if left_window == -1 and right_window == -1:
                return -1
            elif left_window == -1:
                return right_window
            else:
                return left_window