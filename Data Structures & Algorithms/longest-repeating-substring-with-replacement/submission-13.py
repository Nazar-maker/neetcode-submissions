class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        longest = 0
        for c in charSet:
            l = 0
            count = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                else:
                    while r - l + 1 - count > k:
                        if s[l] == c: count -= 1
                        l += 1
                
                longest = max(longest, r - l + 1)
        
        return longest
            

# k = 1
# aaababb
