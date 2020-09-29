"""
You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to
the left, 1 position to the right in the array or stay in the same place  (The pointer should not be
placed outside the array at any time).

Given two integers steps and arrLen, return the number of ways such that your pointer still at
index 0 after exactly steps steps.

Since the answer may be too large, return it modulo 10^9 + 7.
"""


class Solution:
    def __init__(self):
        self.mnem = {}

    def numWays(self, steps: int, arrLen: int) -> int:
        def dp(pos, steps):
            if (pos, steps) in self.mnem:
                return self.mnem[(pos, steps)]
            if steps == 0:
                return 1 if pos == 0 else 0
            if pos < 0:
                return 0
            if pos >= arrLen:
                return 0
            result = dp(pos + 1, steps - 1) + dp(pos - 1, steps - 1) + dp(pos, steps - 1)
            self.mnem[(pos, steps)] = result
            return result

        return dp(0, steps) % (10 ** 9 + 7)


assert Solution().numWays(3, 2) == 4
assert Solution().numWays(10, 5) == 2187
