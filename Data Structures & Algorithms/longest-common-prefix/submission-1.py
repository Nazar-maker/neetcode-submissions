class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minimum = len(strs[0])
        word = strs[0]
        for s in strs:
            if len(s) < minimum: 
                minimum = len(s)
                word = s
        out = ''
        for i in range(minimum):
            for s in strs:
                if s[i] != word[i]: return out
            out += word[i]

        return out    