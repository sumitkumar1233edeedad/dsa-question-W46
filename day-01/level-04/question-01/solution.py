def valid_palindrome(s: str) -> bool:
    """
    Determine if the string can become a palindrome after deleting at most one character.

    Args:
        s: Input string consisting of lowercase English letters.

    Returns:
        True if the string is already a palindrome or can become one by removing at most one character.
    """
    def is_palindrome(left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            # Try skipping either the left or right character
            return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
    return True