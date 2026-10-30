# Trapping Rain Water

- **Day:** `Day 01`
- **Level:** `Level 08`
- **Question:** `Question 01`
- **Difficulty:** `Hard`
- **Topic:** `Two Pointers`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

**Constraints:**
- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

**Example 1:**
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

**Example 2:**
```
Input: height = [4,2,0,3,2,5]
Output: 9
```

**Example 3:**
```
Input: height = [5,4,3,2,1]
Output: 0
Explanation: Strictly decreasing elevation cannot trap any water.
```

---

## 💻 Starter Function

```python
from typing import List

def trap(height: List[int]) -> int:
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> The previous Level 07 problem 'Container With Most Water' introduced the opposite-direction two-pointer pattern where we move the pointer at the shorter line to maximize area. This Level 08 problem evolves that pattern: instead of maximizing a single container, we must accumulate water across all valleys using the same left/right max height tracking. The canonical two-pointer approach (maintaining left_max and right_max while moving the pointer with the smaller max) directly extends the 'move the shorter side' intuition from Container With Most Water into a cumulative summation problem. This avoids duplication by shifting from a single max-area calculation to a total volume accumulation, reinforcing the core two-pointer mechanics of elevation-based boundary tracking.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
