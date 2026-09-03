class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:

        #Approach 1
        # n = len(nums)
        # res = [0]*n
        # for i in range(0, n):
        #     for j in range(0, n):
        #         if nums[j]<nums[i]:
        #             res[i] += 1
        # return res

        #Approach 2
        # sorted_nums = sorted(nums)
        # first_index = {}
        #
        # for i, num in enumerate(sorted_nums):
        #     if num not in first_index:
        #         first_index[num] = i
        #
        # # return [first_index[num] for num in nums]
        #
        # res = [0]*len(nums)
        #
        # for idx, num in enumerate(nums):
        #     res[idx] = first_index[num]
        # return res

        #Approach 3
        freq = [0]*102

        for num in nums:
            freq[num+1] += 1

        for i in range(1, 101):
            freq[i] += freq[i-1]

        return [freq[num] for num in nums]

solution = Solution()
print(solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))