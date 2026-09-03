# 2. Add Two Numbers

- **Difficulty:** Medium
- **Problem Link:** [LeetCode #2](https://leetcode.com/problems/add-two-numbers/)
- **Topic:** Linked List, Math, Recursion

## Problem Description
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contain a single digit. Add two numbers and return the sum as a linked list.

You may assume that the two numbers do not contain any leading `0` except for the digit/number itself.

## Approaches

### 1. Brute Force (Iterative)
- **Intuition:** Since the lists are already given in reverse order, we just `add` the digits in the node of the list and maintain a `carry` value. The `dummy` node acts as an anchor to the head of the new list which is returned at the end of the function. We loop through both the lists till they are exhausted or carry becomes `0`. Inside the loop, we handle `None` case, add the digits, calculate unit place digit and the carry.  
- **Status:** *Accepted*
- **Time Complexity:** $O(max(M, N))$ since the loop runs till the given list is exhausted.
- **Space Complexity:** $O(max(M, N))$ since a new list is created which acts as the solution for the problem.