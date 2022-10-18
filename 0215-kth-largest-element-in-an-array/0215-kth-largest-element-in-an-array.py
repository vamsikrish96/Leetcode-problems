class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def Quickselect(left,right):
            pivot = nums[right]
            for ele in range(left,right):
                if(nums[ele] <= pivot):
                    nums[ele],nums[left] = nums[left],nums[ele]
                    left = left + 1
            nums[left],nums[right] = nums[right],nums[left]
            if(left > k):
                return Quickselect(0,left - 1)
            elif(left < k):
                return Quickselect(left + 1,right)
            else:
                return nums[left]
        return Quickselect(0,len(nums) - 1)      
        