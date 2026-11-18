class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        counter = 0
        max_length = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[counter])
                counter += 1 
            seen.add(s[i])   

            current_length = i - counter + 1
            max_length = max(max_length, current_length)
    
        return max_length