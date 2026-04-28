class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums)-1)

        return nums


    def partition(self, nums, low, high, pivot):
        while low <= high:
            while nums[low] < pivot:
                low += 1
            while nums[high] > pivot:
                high -= 1

            if low <= high:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
                high -= 1
        return low
        

    def quickSort(self, nums, low, high):
        if low < high:
            pivot = nums[(low + high) // 2]
            j = self.partition(nums, low, high, pivot)
            self.quickSort(nums, low, j - 1)
            self.quickSort(nums, j, high)