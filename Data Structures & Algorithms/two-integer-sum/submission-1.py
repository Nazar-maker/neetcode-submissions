class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevValues = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in prevValues: return [prevValues[diff], i]
            prevValues[nums[i]] = i



