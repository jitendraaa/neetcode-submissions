class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            # 1. Create a frequency array for the 26 lowercase English letters
            count = [0] * 26
            
            for char in string:
                # ord() gets the ASCII value. Subtraction maps 'a'->0, 'b'->1, ..., 'z'->25
                count[ord(char) - ord('a')] += 1
                
            # 2. Lists are mutable and CANNOT be dictionary keys. 
            # We convert it to a tuple (immutable) so it can be hashed.
            signature = tuple(count)
            #print(signature)
            result[signature].append(string)

        return list(result.values())
