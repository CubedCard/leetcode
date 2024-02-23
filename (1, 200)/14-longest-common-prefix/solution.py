class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = min(strs, key=len)
        for s in strs:
            common_prefix = ''
            for i, c in enumerate(prefix):
                if c == s[i]:
                    common_prefix += c
                else: 
                    break
            prefix = common_prefix
        return prefix

