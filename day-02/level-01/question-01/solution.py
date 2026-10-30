from typing import List

def reverse_array(nums: List[int]) -> None:
    """
    Reverses the list nums in-place using the two-pointer technique.
    Modifies the input list directly without allocating extra space.
    """
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
