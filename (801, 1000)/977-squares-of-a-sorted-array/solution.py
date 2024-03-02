class Solution(object):
    def sortedSquares(self, nums):
        nums = [num**2 for num in nums]
        nums.sort()
        return nums
        
