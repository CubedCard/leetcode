class Solution(object):
    def singleNumber(self, nums):
        return [x for x in nums if nums.count(x) == 1][0]
        
