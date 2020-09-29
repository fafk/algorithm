"""
Given two sorted arrays, find their median.

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two
sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000

"""
from typing import List
from math import floor


class Solution:
    # TODO the alg can stop after it's readched (m+n)/2 in the new array
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        assert len(nums1) and len(nums2)
        i = 0
        j = 0
        out = []
        while not (i == len(nums1) and j == len(nums2)):
            if i == len(nums1):
                out.append(nums2[j])
                j = j + 1
                continue
            if j == len(nums2):
                out.append(nums1[i])
                i = 1 + i
                continue

            if nums1[i] < nums2[j]:
                out.append(nums1[i])
                i = i + 1
            else:
                out.append(nums2[j])
                j = j + 1

        if len(out) % 2 == 1:
            return out[floor(len(out) / 2)]
        else:
            return (out[floor(len(out) / 2)] + out[floor(len(out) / 2) - 1]) / 2

    def easy_but_slow(self, nums1: List[int], nums2: List[int]) -> float:
        assert len(nums1) and len(nums2)
        out = sorted(nums1 + nums2)
        if len(out) % 2 == 1:
            return out[floor(len(out) / 2)]
        else:
            return (out[floor(len(out) / 2)] + out[floor(len(out) / 2) - 1]) / 2


assert Solution().findMedianSortedArrays([1, 3, 4], [2, 2, 10]) == 2.5 == Solution().easy_but_slow(
    [1, 3, 4], [2, 2, 10])
