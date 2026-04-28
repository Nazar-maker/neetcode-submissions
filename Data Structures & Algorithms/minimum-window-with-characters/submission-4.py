class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        for ts in t:
            countT[ts] = 1 + countT.get(ts, 0)

        out = ''
        length = float('infinity')
        window = {}
        l = 0
        count = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                count += 1

            while count == len(countT):
                if r - l + 1 < length:
                    out = s[l : r+1]
                    length = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    count -= 1

                l += 1
        return out