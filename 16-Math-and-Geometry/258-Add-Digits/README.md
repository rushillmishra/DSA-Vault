# 258. Add Digits

- **Difficulty:** Easy
- **Problem Link:** [LeetCode #258](https://leetcode.com/problems/add-digits/description)
- **Topic:** Math, Simulation, Number Theory

## Problem Description
Given an integer `num`, repeatedly add all its digits until the result has only one digit, and return it.

## Approaches

### 1. Brute Force (Iterative with helper function)
- **Intuition:** It is just the simple simulation of the given problem statement where we keep adding the digits of the number until it is `<10`. I achieved this using a helper function.
- **Status:** *Accepted*
- **Time Complexity:** $O(log n)$, since extracting all digits of a number and adding them takes `log n` operations asymptotically. 
- **Space Complexity:** $O(1)$

### 2. Brute Force (Iterative Nested) 
- **Intuition:** Same as above but without the helper function.
- **Status:** *Accepted*
- **Time Complexity:** $O(log n)$, since extracting all digits of a number and adding them takes `log n` operations asymptotically. 
- **Space Complexity:** $O(1)$

### 3. Digital Root
- **Intuition:** I don't fully understand it myself but the thing is, a number and the sum of its digits always have the `same remainder` when divided by `9`. Hence the formula for it is $[1 + ((num-1) \bmod 9)]$.
- **Status:** *Accepted*
- **TC:** $O(1)$
- **SC:** $O(1)$