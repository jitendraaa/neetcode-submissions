class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        final = []
        for string in strs:
            sstring = "".join(sorted(string))
            #print(sstring)
            if sstring in result:
                result[sstring].append(string)
            else:
                result[sstring] = []
                result[sstring].append(string)
            #print(result)
        return list(result.values())
