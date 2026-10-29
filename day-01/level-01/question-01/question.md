# Reverse String

- **Day:** `Day 01`
- **Level:** `Level 01`
- **Question:** `Question 01`
- **Difficulty:** `Easy`
- **Topic:** `Two Pointers`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array **in-place** with `O(1)` extra memory.

**Constraints:**
- `1 <= s.length <= 10^5`
- `s[i]` is a printable ASCII character.

**Example 1:**
- Input: `s = ["h","e","l","l","o"]`
- Output: `["o","l","l","e","h"]`

**Example 2:**
- Input: `s = ["H","a","n","n","a","h"]`
- Output: `["h","a","n","n","a","H"]`

**Example 3:**
- Input: `s = ["a"]`
- Output: `["a"]`

---

## 💻 Starter Function

```python
def reverseString(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> This is the first question of the curriculum (Day 01, Level 01, Q01). There are no previously solved questions in this sprint. The canonical 'Two-End Traversal' pattern is best introduced with the fundamental in-place reversal algorithm: initializing left/right pointers at the array boundaries, swapping elements, and moving pointers toward the center until they meet. This problem isolates the core mechanics—pointer initialization, loop termination condition (left < right), swap operation, and pointer updates—without additional logic (e.g., conditionals, skipping characters, or arithmetic checks). It avoids duplication because the negative constraint list contains no reversal problems; the avoided titles are all distinct patterns (sliding window, hashing, matrix rotation, etc.). This establishes the baseline for all future two-pointer variations.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
