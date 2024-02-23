class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        if len(s) == 1:
            return 1
        max_len = 0
        start = 0
        end = 0
        while end < len(s):
            if s[end] in s[start:end]:
                start += 1
            else:
                end += 1
                max_len = max(max_len, end - start)
        return max_len
