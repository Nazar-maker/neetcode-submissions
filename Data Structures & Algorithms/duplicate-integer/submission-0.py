class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set()

        for i in nums:
            check.add(i)

        if len(check) != len(nums): return True
        
        return False