class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        maj  = nums[0]
        for ele in nums:
            if(maj == ele):
                count += 1
            elif((maj != ele) and count == 0):
                count,maj = 1,ele
            elif(maj != ele):
                count = count - 1
        return maj