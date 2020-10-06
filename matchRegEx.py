"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Note:

    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


class Solution:
    def readInput(self, p: str) -> str:
        if len(p) == 0:
            return ""
        if len(p) == 1:
            return p
        if p[1] == "*":
            return p[0:2]
        else:
            return p[0]

    def isMatch(self, s: str, p: str) -> bool:
        re_input = self.readInput(p)
        if len(re_input) == 0:
            return not len(s)
        if len(re_input) == 1:
            if len(s) == 0:
                return False
            if s[0] == re_input[0] or re_input[0] == ".":
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        if len(re_input) == 2:
            if self.isMatch(s, p[2:]):
                return True
            for i, char in enumerate(s):  # match 1+
                if char == re_input[0] or re_input[0] == ".":
                    res = self.isMatch(s[i + 1:], p[2:])
                    if res:
                        return True
                else:
                    break
            return False


assert Solution().isMatch("abbbbc", "ab*") is False
assert Solution().isMatch("abbbb", "ab*") is True
assert Solution().isMatch("abb", "ab.") is True
assert Solution().isMatch("abb", ".b.") is True
assert Solution().isMatch("ab", ".*") is True
assert Solution().isMatch("aab", "c*a*b") is True
assert Solution().isMatch("a", "ab*") is True
assert Solution().isMatch("aaaaapple", "a*pple") is True
assert Solution().isMatch("pple", "a*pple") is True
