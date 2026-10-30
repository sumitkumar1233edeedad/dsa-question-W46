def remove_element(nums: list[int], val: int) -> int:
    """
    Removes all occurrences of `val` in `nums` in-place using the two-pointer technique.
    The order of the remaining elements may be changed.
    
    Args:
        nums: List of integers to be modified in-place.
        val: Integer value to remove from the list.
    
    Returns:
        The new length `k` such that the first `k` elements of `nums` are not equal to `val`.
    """
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow