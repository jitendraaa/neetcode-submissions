class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = 0
        for char in s:
            result = result ^ ord(char)

        for char in t:
            result = result ^ ord(char)
        
        if(result == 0):
            return True
        return False