class Solution(object):
    def minimumLength(self, s):
        i, j = 0, len(s) - 1
        while i < j and s[i] == s[j]:
            cur = s[i]
            while i <= j and s[i] == cur:
                i += 1
            while j > i and s[j] == cur:
                j -= 1
        return j - i + 1
