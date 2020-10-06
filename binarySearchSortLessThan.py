"""
Implement function count_numbers that accepts a sorted list of unique integers and, efficiently with
respect to time used, counts the number of list elements that are less than the parameter less_than.

For example, count_numbers([1, 3, 5, 7], 4) should return 2 because there are two list elements less
than 4.

Do this in logarithmic time.
"""

from math import ceil


def count_numbers(sorted_list, less_than):
    if len(sorted_list) == 0:
        return 0
    left = 0
    right = len(sorted_list) - 1
    while left != right:
        mid = ceil((left + right) / 2)
        if sorted_list[mid] > less_than:
            right = mid - 1
        else:
            left = mid

    if sorted_list[left] == less_than:
        return left
    if len(sorted_list) - 1 == left:
        return left + 1
    if left == 0:
        if sorted_list[left] < less_than:
            return 1
        else:
            return 0
    return left + 1


if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 8]
    print(count_numbers(sorted_list, 2))
