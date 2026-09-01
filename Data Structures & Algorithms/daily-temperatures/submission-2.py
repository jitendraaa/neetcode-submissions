class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        result = [0] * size
        stack = []
        for i in range(size):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                temp = stack.pop()
                result[temp] = i - temp
            stack.append(i)
        return result