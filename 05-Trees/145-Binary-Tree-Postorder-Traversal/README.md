# 144. Binary Tree Postorder Traversal

- **Difficulty:** Easy
- **Problem Link:** [LeetCode #145](https://leetcode.com/problems/binary-tree-postorder-traversal)
- **Topic:** Math

## Problem Description
Given the `root` of a binary tree, return the postorder traversal of its nodes' values.

## Approaches

### 1. DFS Traversal / Recursion
- **Intuition:** Postorder Traversal states that the order of visiting nodes in a Binary Tree Traversal is as such: `left -> right -> current`. So to traverse the tree structure from its root node, we use a simple `DFS` recursive function implementing the logic of Preorder Traversal.
- **Status:** *Accepted*
- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(1)$ because no extra memory is used except for the `result` array which stores the traversal.