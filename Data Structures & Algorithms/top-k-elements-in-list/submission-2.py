class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_hashmap = {}
        result = []
        max = 0
        for number in nums:
            count_hashmap[number] = count_hashmap.get(number, 0) + 1
        
        keys = heapq.nlargest(k, count_hashmap, key=count_hashmap.get)
        return keys
        