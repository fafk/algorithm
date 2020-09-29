"""
Given two sorted arrays, merge them into one in-place (without creating another array).
"""
from typing import List


class Solution:
    @staticmethod
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        def shift(arr, j):
            for i in range(len(arr) - 1, j, -1):
                arr[i] = arr[i - 1]
            return arr

        def insert_before(arr, i, val):
            shift(arr, i)
            arr[i] = val
            return arr

        processed_ind = 0
        for j, num2 in enumerate(nums2):
            for i in range(processed_ind, m + processed_ind):
                if num2 < nums1[i]:
                    insert_before(nums1, i, num2)
                    processed_ind = processed_ind + 1
                    break

        # Copy over what's left from nums2
        for i, num in enumerate(nums2[processed_ind:]):
            nums1[m + processed_ind + i] = num
        return nums1


assert Solution().merge([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3) == [-1, 0, 0, 1, 2, 2, 3, 3,
                                                                           3]
assert Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]
assert Solution().merge([0], 0, [1], 1) == [1]
assert Solution().merge([1], 1, [], 0) == [1]
assert Solution().merge([1, 0], 1, [2], 1) == [1, 2]
assert Solution().merge([4, 0, 0, 0, 0, 0], 1, [1, 2, 3, 5, 6], 5) == [1, 2, 3, 4, 5, 6]
