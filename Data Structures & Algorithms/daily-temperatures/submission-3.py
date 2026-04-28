class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0] * len(temperatures)
        for i in range(len(temperatures)):
            r = i
            while temperatures[i] >= temperatures[r]:
                stack.append(temperatures[i])
                r += 1
                if r == len(temperatures): 
                    stack.clear()
                    break
            out[i] = len(stack)
            stack.clear()
        
        return out