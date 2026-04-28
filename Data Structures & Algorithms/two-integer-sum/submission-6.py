class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if nums[i] in prev: return [prev[nums[i]], i]

            prev[diff] = i
                
                