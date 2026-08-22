class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0  
        s = s.replace(" ","").lower()
        right = len(s) - 1
        while left <= right:
            print(s[left], s[right])
            if ((not s[left].isalnum()) and (not s[right].isalnum())):
                    left = left + 1
                    right = right - 1
            elif (not s[left].isalnum()):
                left = left + 1
            elif (not s[right].isalnum()):
                right = right - 1
            elif (s[left] != s[right]):
                    return False
            else:
                left = left + 1
                right = right - 1
            
        return True