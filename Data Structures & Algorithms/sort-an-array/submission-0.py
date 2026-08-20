class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_heap = []
        result = []
        for num in nums:
            heapq.heappush(min_heap,(num))
        for i in range(len(min_heap)):
            result.append(heapq.heappop(min_heap))
        return result