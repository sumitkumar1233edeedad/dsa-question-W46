def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    """
    Finds two indices (1-indexed) in a sorted array that sum to target.
    Uses two-pointer technique.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    # According to problem constraints, there is always exactly one solution.
    # This line should never be reached.
    return []
