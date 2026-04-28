class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        product_without_zero = 1
        zeros = 0
        for i in nums:
            if i == 0:
                product *= i 
                zeros += 1
                continue 
            product *= i
            product_without_zero *= i

        output = []
        if zeros > 1: return [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0: 
                output.append(product_without_zero)
                continue
            output.append(int(product // nums[i]))
        
        return output