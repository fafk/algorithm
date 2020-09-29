"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Solution:
    def __init__(self):
        self.mnem = {}

    def climbStairs(self, n: int) -> int:
        if n in self.mnem:
            return self.mnem[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        res = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.mnem[n] = res
        return res