# 1523. Count Odd Numbers in an Interval Range

- **Difficulty:** Easy
- **Problem Link:** [LeetCode #1523](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/)
- **Topic:** Math

## Problem Description
Given two non-negative integers `low` and `high`, return the count of odd numbers between `low` and `high` (inclusive).

## Approaches

### 1. Brute Force (Iterative)
- **Intuition:** Iterate through every integer from `low` to `high` (inclusive) and check parity. If `i % 2 != 0`, increment the counter.
- **Status:** *Time Limit Exceeded (TLE)*
- **Time Complexity:** $O(n)$, where $n = high - low + 1$
- **Space Complexity:** $O(1)$

### 2. Optimal (Mathematical Prefix Count)
- **Intuition:** The count of odd numbers in the range $[1, n]$ is given by $\lfloor (n + 1) / 2 \rfloor$. Thus, the total odd numbers in $[low, high]$ equals:
  $$\text{countOdds}(high) - \text{countOdds}(low - 1) = \frac{high + 1}{2} - \frac{low}{2}$$
- **Status:** *Accepted*
- **Time Complexity:** $O(1)$
- **Space Complexity:** $O(1)$