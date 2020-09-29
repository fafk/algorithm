"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the
latest version of your product fails the quality check. Since each version is developed based on the
previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes
all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement
a function to find the first bad version. You should minimize the number of calls to the API.
"""

from math import floor


class Solution:
    def __init__(self, i):
        self.badVersionPosition = i

    def isBadVersion(self, n):
        return True if self.badVersionPosition <= n else False

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        if left == right:
            return right
        while left + 1 != right:
            mid = floor((left + right) / 2)
            if not self.isBadVersion(mid):
                left = mid
            else:
                right = mid
        return right if self.isBadVersion(right) else left


assert Solution(7).firstBadVersion(500) == 7
assert Solution(500).firstBadVersion(500) == 500
