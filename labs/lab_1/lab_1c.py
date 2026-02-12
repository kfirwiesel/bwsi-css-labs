"""
lab_1c.py

Given a list of numbers, return the maximum sum of any contiguous subarray of the list.

Do not assume anything. Account for all edge cases.

Derived from LeetCode problem: https://leetcode.com/problems/maximum-subarray/ (leetcode medium)
"""

# TODO: Find and resolve the bug in the following implementation. Create unit tests to verify your fix.
def max_subarray_sum(nums: list[int]) -> int:
    """
    Function that takes in a list of integers and returns the maximum sum of any contiguous subarray.

    Args:
        nums (list[int]): List of integers.

    Returns:
        int: The maximum sum of any contiguous subarray.
    """

    if not nums:
        raise IndexError("Array cannot be empty.")
    else:

        max_value = nums[0]
        
        for start in range(len(nums)):
            value = 0
            for num in range(start, len(nums)):
                value += nums[num]
                max_value = max(value, max_value)
                
        return max_value

# Example usage:
def main():
    nums = [1, 2, 3, 4, 5, 6]
    result = max_subarray_sum(nums)
    print(f"Maximum subarray sum: {result}")

if __name__ == "__main__":
    main()