from itertools import permutations

class Solution(object):
    def getPermutation(self, n, k):
        arr = [x + 1 for x in range(n)]
        perms = permutations(arr)
        return ''.join(map(str, list(perms)[k - 1]))
