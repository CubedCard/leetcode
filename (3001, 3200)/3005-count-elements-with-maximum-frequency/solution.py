class Solution(object):
    def maxFrequencyElements(self, nums):
        counts = {num: nums.count(num) for num in nums}
        max_count = max(counts.values())
        return max_count * len([num for num, count in counts.items() if count == max_count])
