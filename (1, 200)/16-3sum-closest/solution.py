class Solution(object):
    def threeSumClosest(self, nums, target):
        if 3 > len(nums) > 500:
            return 0
        if any(x < -10**3 or x > 10**3 for x in nums):
            return 0
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                if abs(s - target) < abs(result - target):
                    result = s
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
        return result
