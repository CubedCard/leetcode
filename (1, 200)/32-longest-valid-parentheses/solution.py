class Solution(object):
    def fastLongestValidParentheses(self, s):
        stack = [-1]
        max_length = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_length = max(max_length, i - stack[-1])
                else:
                    stack.append(i)
        return max_length

    def longestValidParentheses(self, s):
        i, j = 0, len(s) - 1
        if i >= j:
            return 0
        if (self.isValid(s)):
            return j - i + 1
        return max(self.longestValidParentheses(s[i+1:]), self.longestValidParentheses(s[:j]))

    def isValid(self, s):
        chars = '()'
        counts = {c: s.count(c) for c in chars}
        for i in range(0, len(chars),2):
            if counts[chars[i]] != counts[chars[i+1]]:
                return False

        while '()' in s:
            s = s.replace('()', '')
        return s == ''
