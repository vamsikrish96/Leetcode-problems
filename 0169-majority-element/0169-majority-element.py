class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        result,max_count = 0,0
        for ele in nums:
            count[ele] = 1 + count.get(ele,0)
            if(count[ele] > max_count):
                max_count = count[ele]
                result = ele
        return result