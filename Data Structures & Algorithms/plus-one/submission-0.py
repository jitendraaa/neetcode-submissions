class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        prev = 1
        for digit in range(len(digits)-1, -1, -1):
            if digits[digit] + prev <= 9:
                digits[digit] += prev
                break
            elif digits[digit] + prev > 9:
                digits[digit] = (digits[digit]+prev)%10
                prev = 1
            if prev == 1 and digit == 0:
                result = [1]
                result.extend(digits)
                return result
        return digits