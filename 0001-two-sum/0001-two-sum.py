class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i in range(len(nums)):
            if(nums[i] in result):
                return result[nums[i]],i
            else:
                temp = target - nums[i]
                result[temp] = i

        