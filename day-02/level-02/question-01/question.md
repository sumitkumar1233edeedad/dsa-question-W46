# Remove Target Value In-Place

- **Day:** `Day 02`
- **Level:** `Level 02`
- **Question:** `Question 01`
- **Difficulty:** `Easy`
- **Topic:** `Two Pointers`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **in-place**. The order of the elements may be changed. Return the number of elements in `nums` which are not equal to `val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`. To get accepted, you need to do the following things:

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
def remove_element(nums: list[int], val: int) -> int:
    """
    Removes all occurrences of val in nums in-place using fast/slow pointers.
    Returns the new length k.
    """
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> The previous problem (Day 02 Level 01) practiced the classic left/right two-pointer pattern for reversing an array. The logical next step for 'Fast & Slow Runners - Part 1' is the same-direction pointer pattern for in-place array filtering. 'Remove Element' is the canonical introductory problem for this mechanic: a fast pointer scans the array while a slow pointer tracks the position to write valid (non-target) elements. This avoids duplication of the explicitly forbidden 'Move Zeroes' and 'Remove Duplicates from Sorted Array' while teaching the exact same core algorithmic primitive (overwriting with a write pointer) that underpins those problems. It reinforces the invariant that the slow pointer always points to the next write location for a valid element.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
