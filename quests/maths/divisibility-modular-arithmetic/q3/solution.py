class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = []
        for x in range(left, right + 1):
            xstr = str(x)
            add = True
            for c in xstr:
                if int(c) == 0 or x % int(c) != 0:
                    add = False
            if add:
                nums.append(x)
        return nums
