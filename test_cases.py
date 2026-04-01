def find_two_sum(nums, target):
    """
    Finds two numbers in the list that add up to the target value.
    Returns a tuple of the two numbers if found, otherwise None.
    """
    seen = {}
    for num in nums:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen[num] = True
    return None

# Example usage:
# result = find_two_sum([2, 7, 11, 15], 9)
# print(result)  # Output: (2, 7)

import pytest

def find_two_sum(nums, target):
    seen = {}
    for num in nums:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen[num] = True
    return None

def test_find_two_sum_basic():
    assert find_two_sum([2, 7, 11, 15], 9) == (2, 7)

def test_find_two_sum_negative_numbers():
    assert find_two_sum([-1, -2, -3, -4], -5) == (-2, -3)

def test_find_two_sum_no_solution():
    assert find_two_sum([1, 2, 3], 7) is None

def test_find_two_sum_empty_list():
    assert find_two_sum([], 0) is None

def test_find_two_sum_single_element():
    assert find_two_sum([5], 5) is None

def test_find_two_sum_duplicate_numbers():
    # Should find the pair if the target is double one of the numbers
    assert find_two_sum([3, 3], 6) == (3, 3)

def test_find_two_sum_large_numbers():
    assert find_two_sum([1000000, 2000000, 3000000], 5000000) == (2000000, 3000000)

def test_find_two_sum_order_independence():
    # The function returns the complement first, then the current number
    assert find_two_sum([10, 2], 12) == (10, 2)
    assert find_two_sum([2, 10], 12) == (2, 10)