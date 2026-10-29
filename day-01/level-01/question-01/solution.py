def reverseString(s: list[str]) -> None:
    """
    Reverses the input list of characters in-place.

    Args:
        s: List of single-character strings representing the string to reverse.
    Returns:
        None. The list `s` is modified in-place.
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
