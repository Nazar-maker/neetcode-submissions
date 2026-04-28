class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_group = []
        out = []
        for s in strs:
            count = {}
            for i in range(len(s)):
                count[s[i]] = 1 + count.get(s[i], 0)

            if count in anagram_group:
                i = anagram_group.index(count)
                out[i].append(s)
                continue
            anagram_group.append(count)
            out.append([s])
        return out
    