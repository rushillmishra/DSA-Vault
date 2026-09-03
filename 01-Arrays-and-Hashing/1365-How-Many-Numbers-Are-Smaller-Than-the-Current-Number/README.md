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
- **Time Complexity:** $O(n^2)$ since we compare each element with every other element, exhaustive in nature.
- **Space Complexity:** $O(n)$ since we have to return the answer as an array of equal size.

### 2. Using Sorting (Comparison Based)
- **Intuition:** In an array sorted in increasing order of elements, element `nums[i]` is less than or equal to element `nums[i+1]` and it holds true for every element thereafter. So to speak, the number of elements less than a number in a sorted array is the index `i` of its first appearance in the sorted array.
- **Status:** *Accepted*
- **Time Complexity:** $O(n log n)$ since we sort the array to get the first occurence of a number in the array.
- **Space Complexity:** $O(n)$ since an extra array is created to store the sorted `nums` array. Also we return an array `res` 
which is equal to the size of original array.

### 3. Optimized (Counting Sort)
- **Intuition:** The constraints of the problem are relatively low: `2 <= nums.length <= 500` and `0 <= nums[i] <= 100` so simply create a frequency array which counts the frequency of each `nums[i]`. After frequency is calculated, prefix sum is calculated using the frequency array. In the end, a array is returned using the prefix sum which is the answer.
- **Status:** *Accepted*
- **Time Complexity:** $O(n)$ since it takes that much time to traverse through original `nums` array to populate the frequency array.
- **Space Complexity:** $O(1)$ since the auxiliary space does not scale with the size of the array.

### 4. Optimized Counting Sort with Max_Num
- **Intuition:** Initializing a frequency array of size 102 everytime might result in creation of sparse matrix and waste a lot of space if the maximum element of nums is small so instead of initializing the array with 102 indices, calculate the maximum element of the array and create a frequency array of that size to reduce wastage of space.
- **Status:** *Accepted*
- **TC:** $O(n)$ since it takes that much time to traverse through original array to populate the frequency array.
- **SC:** $O(max(n))$ since now the frequency array is created according to the max element present in nums. 