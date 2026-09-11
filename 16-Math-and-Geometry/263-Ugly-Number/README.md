# 263. Ugly Number

- **Difficulty:** Easy
- **Problem Link:** [LeetCode #263](https://leetcode.com/problems/ugly-number)
- **Topic:** Math

## Problem Description
An **ugly number** is a positive integer which does not have a prime factor other than 2, 3, and 5.

Given an integer `n`, return `true` *if* `n` is an **ugly number**.

## Approaches

### 1. Brute Force (Iterative)
- **Intuition:** First I check for the following conditions: 
  - Whether the number is positive or not
  - Whether the number is 1 which has no prime factor (an empty subset of prime factors)
  - Whether the number is subset of given set i.e. is number itself 2 or 3 or 5 

If the number is positive but fails the last two condition, we simply check if after dividing it by the prime factos (2, 3, 5) it results to 1 or not. If it does then it is an ugly number else not.
- **Status:** *Accepted*
- **Time Complexity:** $O(log n)$ since at each iteration the number is reduced by any of the factors. 
- **Space Complexity:** $O(1)$
