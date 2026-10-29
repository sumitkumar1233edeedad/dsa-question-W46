# Two Sum in Sorted Array

- **Day:** `Day 01`
- **Level:** `Level 03`
- **Question:** `Question 01`
- **Difficulty:** `Easy`
- **Topic:** `Two Pointers`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, **added by one** as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

**Constraints:**
- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in **non-decreasing order**.
- `-1000 <= target <= 1000`
- Only one valid answer exists.

**Example 1:**
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```

**Example 2:**
```
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3.
```

**Example 3:**
```
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2.
```

---

## 💻 Starter Function

```python
def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> Previous problems (Reverse String, Remove Element) introduced opposite-direction pointers on strings and fast/slow pointers for in-place mutation. This problem is the canonical introduction to the 'Sorted Target Sum' pattern: leveraging the sorted property to converge two pointers from opposite ends based on the comparison between current sum and target. It establishes the fundamental binary pointer convergence mechanic (move left if sum > target, right if sum < target) without the complexity of duplicate handling or triplet search, making it the ideal Level 3 entry point.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
