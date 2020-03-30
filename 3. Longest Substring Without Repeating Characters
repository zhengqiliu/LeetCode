class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        end = 0
        max_length = 0
        visited = set()
        for i in range(len(s)):
            while end < len(s) and s[end] not in visited:
                visited.add(s[end])
                end += 1
            max_length = max(max_length, end-i)
            visited.remove(s[i])
        
        return max_length
