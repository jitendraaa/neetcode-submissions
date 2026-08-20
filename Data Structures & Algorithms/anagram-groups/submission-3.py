class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            sstring = "".join(sorted(string))
            result[sstring].append(string)
        return list(result.values())
