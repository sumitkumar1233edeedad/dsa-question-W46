def check_pair_sum_exists(numbers: list[int], target: int) -> bool:
    """
    Determines if there exist two distinct indices i and j in a sorted array
    such that numbers[i] + numbers[j] == target.

    Args:
        numbers: A list of integers sorted in non-decreasing order (1-indexed in problem, but 0-indexed here).
        target: The target sum.

    Returns:
        True if such a pair exists, False otherwise.
    """
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return False
