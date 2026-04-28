class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        
        for l in range(len(temperatures)-1):
            r = l + 1
            while r < len(temperatures) and temperatures[l] >= temperatures[r]:
                r += 1
            if r == len(temperatures): r = l
            output[l] = r - l
        return output