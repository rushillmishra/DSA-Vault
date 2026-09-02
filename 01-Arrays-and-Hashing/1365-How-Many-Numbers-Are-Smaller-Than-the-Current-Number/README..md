# 1365. How Many Numbers Are Smaller Than the Current Number

- **Difficulty:** Easy
- **Problem Link:** [LeetCode #1365](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/)
- **Topic:** Array, Hash Table, Sorting

## Problem Description
Given the array `nums`, for each `nums[i]` find out how many numbers in the array are smaller than it. That is, for each `nums[i]` you have to count the number of valid `j's` such that `j != i` and `nums[j] < nums[i]`. 

Return the answer in an array.

## Approaches

### 1. Brute Force (Iterative)
- **Intuition:** We create a `res` array of length equal to length of`nums` and initialize each value with `0`. After that, we run a nested loop and check `nums[i]` against `nums[j]`, incrementing the value in `res`.
- **Status:** *Accepted*
- **Time Complexity:** $O(n^2)$
- **Space Complexity:** $O(n)$ since we have to return the answer as an array of equal size.

