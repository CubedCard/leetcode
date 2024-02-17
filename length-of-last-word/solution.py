class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split(" ")
        for i in range(len(words)):
            if len(words[(len(words) - 1 - i)]) > 0:
                return len(words[(len(words) - 1 - i)])
