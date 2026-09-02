class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        if right == 0:
            return nums[0]
        while left <= right:
            mid = left + (right-left)//2

            if(mid == 0 and nums[mid]<nums[mid+1] and nums[mid]<nums[len(nums)-1]):
                return nums[mid]
            elif(mid == len(nums)-1 and nums[mid]<nums[mid-1] and nums[mid]<nums[0]):
                return nums[mid]
            elif(mid>0 and mid<len(nums) and(nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1])):
                return nums[mid]
            elif(nums[mid]<nums[len(nums)-1]):
                right = mid-1
            else:
                left = mid + 1
            