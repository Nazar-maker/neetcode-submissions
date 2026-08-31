class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [None]*len(nums)
        def solve(i):
            if i >= len(nums):
                return 0
            if memo[i]:
                return memo[i]
            skip = solve(i+1)
            rob = nums[i] + solve(i+2)
            memo[i] = max(skip, rob)
            return memo[i]

        return solve(0)