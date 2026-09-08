class Solution:
    def isHappy(self, n: int) -> bool:
        history = set()
        while n > 0:
            if n in history:
                return False
            elif n == 1:
                return True
            else:
                history.add(n)
            digit_sum = 0
            while n > 0:
                digit_sum = digit_sum + ((n%10)**2)
                n = n // 10
            n = digit_sum
        return False