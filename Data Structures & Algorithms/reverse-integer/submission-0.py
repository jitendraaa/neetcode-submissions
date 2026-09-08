class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        INT_MIN, INT_MAX, result = -2**31, 2**31-1, 0
        x = abs(x)
        while x != 0:
            pop = x % 10
            x = x//10
            
            if result > INT_MAX//10 or (result == INT_MAX and pop > 7):
                return 0
            result = result * 10 + pop
        return result * sign
