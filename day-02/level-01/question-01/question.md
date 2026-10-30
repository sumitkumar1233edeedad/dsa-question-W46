# Reverse Array In-Place

- **Day:** `Day 02`
- **Level:** `Level 01`
- **Question:** `Question 01`
- **Difficulty:** `Easy`
- **Topic:** `Two Pointers`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an array of integers `nums`, reverse the array **in-place**. You must modify the input array directly without allocating extra space for another array (i.e., O(1) extra memory).

Use the two-pointer technique: initialize one pointer at the start (`left`) and one at the end (`right`), swap the elements, then move the pointers toward the center until they meet.

**Constraints:**
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

**Example 1:**
```
Input: nums = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
```

**Example 2:**
```
Input: nums = [10, -2, 3, 7]
Output: [7, 3, -2, 10]
```

**Example 3:**
```
Input: nums = [42]
Output: [42]
```

---

## 💻 Starter Function

```python
from typing import List

def reverse_array(nums: List[int]) -> None:
    """
    Reverses the list nums in-place.
    """
    # Your code here
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> The previous day (Day 01) covered advanced two-pointer problems such as 3-Sum, Container With Most Water, Trapping Rain Water, and Palindrome with One Deletion. Those problems assume familiarity with the basic two-end traversal pattern. Today starts a new week at Level 01 (the most fundamental level), so the logical first problem is the canonical in-place array reversal. This problem isolates the core mechanic—left/right pointers meeting at the center while swapping elements—without any additional conditions (like target sums, area calculations, or palindrome checks). It avoids duplication because none of the previously solved problems was a simple reversal task. Mastering this pattern here sets the foundation for the more complex two-pointer variations that will appear later in the week.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
