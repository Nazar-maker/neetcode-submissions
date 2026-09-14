class Solution:
    def longestPalindrome(self, s: str) -> str:
        first_index = 0
        length = 0
        dp = [[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i, -1, -1):
                if s[i] == s[j] and (i-j<=2 or dp[i-1][j+1]):
                    dp[i][j] = True
                    if (i-j+1) > length: 
                        length = i-j+1
                        first_index = j
        
        return s[first_index:first_index+length]