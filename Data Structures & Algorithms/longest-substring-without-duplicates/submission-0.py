class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        longest = 0
        l = 0
        for r in range(len(s)):
            while s[r] in substring:
                substring.remove(s[l])
                l += 1
            
            length = r - l + 1
            longest = max(longest, length)
            substring.add(s[r])
        
        return longest
            