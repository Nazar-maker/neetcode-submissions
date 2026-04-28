class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(heights) - 1

        while l <= r:
            height = min(heights[l], heights[r])
            width = r - l
            maxArea = max(maxArea, height*width)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea



# 4, 2, 3, 6, 3, 2, 5
# 2 2 2: 2x