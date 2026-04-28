class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        out = []

        for i in range(2*len(nums)):
            if i < len(nums):
                out.append(nums[i])
            else:
                out.append(nums[i - len(nums)])

        return out