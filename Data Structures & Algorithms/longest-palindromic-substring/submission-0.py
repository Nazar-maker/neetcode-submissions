class Solution:
    def longestPalindrome(self, s: str) -> str:
        first_index = 0
        length = 0

        for i in range(len(s)):
            # if the selected character length is odd
            l = r = i
            while l>=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > length:
                    length = r-l+1
                    first_index = l

                l -= 1
                r += 1

            # if the selected charater length is even
            l = i
            r = i + 1
            while l>=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > length:
                    length = r-l+1
                    first_index = l
                l -= 1
                r += 1

        return s[first_index:first_index+length]
                


