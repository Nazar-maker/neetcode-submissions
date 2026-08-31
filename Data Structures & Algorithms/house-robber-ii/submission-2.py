class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = [[-1]*2 for _ in range(len(nums))]

        def solve(i, flag):
            if i >= len(nums) or (i == len(nums)-1 and flag):
                return 0
            if memo[i][flag] != -1:
                return memo[i][flag]
            memo[i][flag] = max(solve(i+1, flag), nums[i] + solve(i+2, flag or i==0))
            return memo[i][flag]

        return max(solve(0, True), solve(1, False))