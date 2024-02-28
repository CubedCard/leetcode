import itertools

class Solution(object):
    def oldSolution(self, nums):
        seen = set()
        permutations = [perm for perm in itertools.permutations(nums) if perm not in seen and not seen.add(perm)]
        permutations.sort()
        next_index = permutations.index(tuple(nums)) + 1
        if next_index == len(permutations):
            for i in range(len(nums)):
                nums[i] = permutations[0][i]
        else:
            for i in range(len(nums)):
                nums[i] = permutations[next_index][i]

    def nextPermutation(self, nums):
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i < 0:
            nums.reverse()
            return

        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[i+1:][::-1]
