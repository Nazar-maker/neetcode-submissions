class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # self.quickSort(nums, 0, len(nums)-1)
        self.mergeSort(nums, 0, len(nums)-1)

        return nums

    
    
    def merge(self, nums, low, mid, high):
        left, right = nums[low:mid+1], nums[mid+1:high+1]

        i, j, k = low, 0, 0

        while j < len(left) and k < len(right):
            if left[j] <= right[k]:
                nums[i] = left[j]
                j += 1
            else:
                nums[i] = right[k]
                k += 1
            i += 1

        while j < len(left):
            nums[i] = left[j]
            i += 1
            j += 1
        
        while k < len(right):
            nums[i] = right[k]
            i += 1
            k += 1

    # def partition(self, nums, low, high, pivot):
    #     while low <= high:
    #         while nums[low] < pivot:
    #             low += 1
    #         while nums[high] > pivot:
    #             high -= 1

    #         if low <= high:
    #             nums[low], nums[high] = nums[high], nums[low]
    #             low += 1
    #             high -= 1
    #     return low
        

    # def quickSort(self, nums, low, high):
    #     if low < high:
    #         pivot = nums[(low + high) // 2]
    #         j = self.partition(nums, low, high, pivot)
    #         self.quickSort(nums, low, j - 1)
    #         self.quickSort(nums, j, high)

    def mergeSort(self, nums, low, high):
        if low >= high: return
        mid = (low + high) // 2
        self.mergeSort(nums, low, mid)
        self.mergeSort(nums, mid+1, high)
        self.merge(nums, low, mid, high)

