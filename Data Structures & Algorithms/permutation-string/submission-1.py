class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size1 = len(s1)
        size2 = len(s2)
        if size2 < size1:
            return False
        s1_counts = Counter(s1)
        window_counts = Counter(s2[:size1])

        if s1_counts == window_counts:
            return True
        
        for i in range(size1, size2):
            window_counts[s2[i]] += 1
            left_char = s2[i-size1]
            if window_counts[left_char]==1:
                del window_counts[left_char]
            else:
                window_counts[left_char]-=1
            if s1_counts == window_counts:
                return True

        return False