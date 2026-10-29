from typing import List

def remove_element(nums: List[int], val: int) -> int:
    """
    Removes all occurrences of `val` in `nums` in-place using the two-pointer technique.
    The order of elements may be changed. Returns the new length `k` such that the first
    `k` elements of `nums` are the elements not equal to `val`.

    Args:
        nums: List of integers to process.
        val: Integer value to remove from `nums`.

    Returns:
        The number of elements in `nums` that are not equal to `val`.
    """
    # slow pointer points to the position where the next non-val element should be placed
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow
