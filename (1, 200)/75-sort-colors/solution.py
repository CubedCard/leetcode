class Solution(object):
    def sortColors(self, nums):
        def merge_sort(nums, start, end):
            if start >= end:
                return
            mid = (start + end) / 2
            merge_sort(nums, start, mid)
            merge_sort(nums, mid + 1, end)
            merge(nums, start, mid, end)

        def merge(nums, start, mid, end):
            left = nums[start:mid + 1]
            right = nums[mid + 1:end + 1]
            i = j = 0
            for k in range(start, end + 1):
                if i < len(left) and (j >= len(right) or left[i] <= right[j]):
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1

        merge_sort(nums, 0, len(nums) - 1)
