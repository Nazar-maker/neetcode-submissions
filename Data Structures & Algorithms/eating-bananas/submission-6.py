import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxE = max(piles)
        l, r = 1, maxE
        out = r
        while l <= r:
            mid = (l + r) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / mid)
            if totalTime <= h:
                out = mid
                r = mid - 1
            else:
                l = mid + 1
        return out

        