# 3870. Count Commas In a Range

- **Difficulty:** Easy
- **Problem Link:** [LeetCode #3870](https://leetcode.com/problems/count-commas-in-range/description)
- **Topic:** Math

## Problem Description
You are given an integer `n`.

Return the total number of commas used when writing all integers from `[1, n]` (inclusive) in standard number formatting.

In standard formatting:

- A comma is inserted after every three digits from the right.

- Numbers with fewer than 4 digits contain no commas.

## Approaches

### 1. Brute Force 
- **Intuition:** Since numbers less than 1000 do not have  a comma in them and each number has as many commas in it as the difference between `n` and `999` due to loose constraint $n<=10^5$. In simple words, find difference between `n` and `999`.
- **Status:** *Accepted*
- **Time Complexity:** $O(1)$
- **Space Complexity:** $O(1)$

