# Remove Element

- **Day:** `Day 01`
- **Level:** `Level 02`
- **Question:** `Question 01`
- **Difficulty:** `Easy`
- **Topic:** `Two Pointers`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **in-place**. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:

*   Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.
*   Return `k`.

**Constraints:**
*   `0 <= nums.length <= 100`
*   `0 <= nums[i] <= 50`
*   `0 <= val <= 100`

**Example 1:**
```
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2. It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Example 2:**
```
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,3,0,4,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4. Note that the five elements can be returned in any order.
```

**Example 3:**
```
Input: nums = [], val = 5
Output: 0, nums = []
```

---

## 💻 Starter Function

```python
from typing import List

def remove_element(nums: List[int], val: int) -> int:
    """
    Removes all occurrences of val in nums in-place using fast/slow pointers.
    Returns the new length k.
    """
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> The previous problem (Reverse String) utilized opposite-direction two pointers (left/right) converging towards the center. This problem introduces the complementary 'Fast & Slow Runner' pattern (same-direction pointers) which is the canonical approach for in-place array filtering/transformation. It teaches the core mechanic of using a slow pointer to track the write position and a fast pointer to scan/read elements, effectively solving the 'Remove Element' problem. This avoids duplication of 'Move Zeroes' or 'Remove Duplicates from Sorted Array' (which are specific applications of this exact pattern) while establishing the fundamental runner technique required for those harder variants later in the curriculum.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
