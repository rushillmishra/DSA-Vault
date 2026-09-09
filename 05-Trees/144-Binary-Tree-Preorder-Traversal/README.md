# 144. Binary Tree Preorder Traversal

- **Difficulty:** Easy
- **Problem Link:** [LeetCode #144](https://leetcode.com/problems/binary-tree-preorder-traversal)
- **Topic:** Math

## Problem Description
Given the `root` of a binary tree, return the preorder traversal of its nodes' values.

## Approaches

### 1. DFS Traversal / Recursion
- **Intuition:** Preorder Traversal states that the order of visiting nodes in a Binary Tree Traversal is as such: `current -> left -> right`. So to traverse the tree structure from its root node, we use a simple `DFS` recursive function implementing the logic of Preorder Traversal.
- **Status:** *Accepted*
- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(1)$ because no extra memory is used except for the `result` array which stores the traversal.

